"""Entrypoint of the app"""
from telegram.ext import ApplicationBuilder, CommandHandler

from {{cookiecutter.project_slug}}.entities import Config
from {{cookiecutter.project_slug}}.callbacks import (
    start, bot_help
)


def run(cfg: Config):
    """
    Entrypoint of the service.
    Parameters:
    -----------
    - cfg: wallet_sniffer.entities.Config
        The Config instance for the service.
    """
    application = ApplicationBuilder().token(cfg.bot_apikey).build()

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', bot_help)

    application.add_handler(start_handler)
    application.add_handler(help_handler)

    application.run_polling()
