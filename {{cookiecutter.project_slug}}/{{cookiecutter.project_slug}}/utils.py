"""
Utils to be used around the bot
"""
import structlog
from telegram import Update


def get_username(update: Update):
    """
    Get the username from the update object.
    Parameters:
    -----------
    - update: telegram.Update object
    Returns:
    --------
    - username: str
        The username of the user that sent the message.
    """
    if hasattr(update, "message"):
        return update.message.from_user.username
    if hasattr(update, "callback_query"):
        return update.callback_query.message.chat.username
    raise AttributeError()


def get_user_id(update: Update):
    """
    Get the telegram user id from the update object.
    Parameters:
    -----------
    - update: telegram.Update object
    Returns:
    --------
    - user_id: str
        The user id of the user that sent the message.
    """
    if hasattr(update, "message"):
        return update.message.from_user.id
    if hasattr(update, "callback_query"):
        return update.callback_query.message.chat.id
    raise AttributeError()
