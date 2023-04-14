"""
Logging requests messages
"""
import time
import uuid

import structlog

from telegram import Update
from telegram.ext import CallbackContext

from {{cookiecutter.project_slug}}.utils import get_username, get_user_id


logger = structlog.get_logger()


class Results():
    """
    Events to finallize requests
    """
    SUCCESS = "success"
    CANCELLED = "cancelled"
    ERROR = "error"


def request_arrived(update: Update, context: CallbackContext, action: str):
    """
    Performs the configuration needed for every request that arrives.
    Parameters:
    -----------
    - update: telegram.Update object
    - context: telegram.ext.ContextTypes.DEFAULT_TYPE object
    - action: str
        The action that the user sent to the bot.
    """
    username = get_username(update)
    user_id = get_user_id(update)
    request_id = str(uuid.uuid4())
    context.user_data['request_id'] = request_id
    context.user_data['username'] = username
    context.user_data['id'] = user_id
    add_request_arrived_data(context, action, username, user_id, request_id)
    logger.info("request_arrived", action=action, username=username, user_id=user_id, request_id=request_id)


def add_request_arrived_data(context: CallbackContext, action: str, username: str, user_id: str, request_id: str):
    """
    Add request arrived data and application metadata to the context.
    Parameters:
    -----------
    - context: telegram.ext.ContextTypes.DEFAULT_TYPE object
    - action: str
        The action that the user sent to the bot.
    - username: str
        The username of the user that sent the message.
    - user_id: str
        The telegram id of the user that sent the message.
    """
    context.user_data['event_info'] = {
        "metadata": {
            "service": "telegram-bot",
            "integrator": ""
        },
        "request": {
            "action": action,
            "username": username,
            "user_id": user_id,
            "result": None,
            "request_id": request_id,
            "start_time": current_milliseconds(),
            "end_time": None,
            "elapsed": None,
        }
    }


def current_milliseconds():
    """
    Get the current time in milliseconds.
    Returns:
    --------
    - current_time: int
    """
    return round(time.time() * 1000)


def save_request_data(context: CallbackContext, result: Results):
    event_info = get_event_info(context)
    end_time = current_milliseconds()
    event_info['request']['end_time'] = end_time
    elapsed = end_time - event_info['request']['start_time']
    event_info['request']['elapsed'] = elapsed
    event_info['request']['result'] = result


def request_served(update: Update, context: CallbackContext,
                   result: Results = Results.SUCCESS):  # pylint: disable=unused-argument
    """Request served function"""
    if 'request_id' not in context.user_data:
        logger.warning('request_served_no_request_id')
        return

    save_request_data(context, result)
    request_id = context.user_data['request_id']
    kpis = context.user_data

    logger.info("request_served", request_id=request_id, result=result, kpis=kpis)
    clear_user_data(context)


def get_event_info(context: CallbackContext):
    return context.user_data['event_info']


def clear_user_data(context: CallbackContext):
    context.user_data.clear()

def update_context_with_request_data(context: CallbackContext, key: str, **kwargs):
    context.user_data['event_info'][key] = kwargs
