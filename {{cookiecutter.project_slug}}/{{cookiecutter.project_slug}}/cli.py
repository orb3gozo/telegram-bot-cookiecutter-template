"""
Command-line interface that acts as the entrypoint from which the server can be started.
"""
import os
import click

from {{cookiecutter.project_slug}} import __version__
from {{cookiecutter.project_slug}} import app
from {{cookiecutter.project_slug}} import config


@click.command()
def main():
    """
    Entrypoint of the app.
    To run it, simply put this command in your terminal:
    ```bash
    python wallet_sniffer/cli.py
    ```
    """
    logs_path = os.getenv("BOT_LOGS_PATH", "/tmp")
    artifacts_path = os.getenv("BOT_ARTIFACTS_PATH", "/tmp")
    
    config.initialize_loggers()
    config.create_application_directories(logs_path, artifacts_path)
    cfg = config.load_configuration(artifacts_path, logs_path)
    
    app.run(cfg)
    

if __name__ == "__main__":  # pragma: no cover
    main()
