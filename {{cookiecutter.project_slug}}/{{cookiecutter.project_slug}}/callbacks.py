"""All Bot Callbacks"""
from telegram import Update
from telegram.ext import ContextTypes

from {{cookiecutter.project_slug}}.logging_requests import (
    request_arrived, request_served, Results
)
from {{cookiecutter.project_slug}}.strings import dialogs, ENGLISH


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Callback for the /start command.
    Parameters:
    -----------
    - update: telegram.Update object
    - context: telegram.ext.ContextTypes.DEFAULT_TYPE object
    - files_max_size: int
    """
    await bot_help(update, context, command="/start")


async def bot_help(update: Update, context: ContextTypes.DEFAULT_TYPE, command: str = "/help") -> None:
    """
    Callback for the /help command.
    Parameters:
    -----------
    - update: telegram.Update object
    - context: telegram.ext.ContextTypes.DEFAULT_TYPE object
    - files_max_size: int
    - command: str
    """
    request_arrived(update, context, action=command)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=dialogs['help'][ENGLISH])
    request_served(update, context, result=Results.SUCCESS)
