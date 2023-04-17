<div align="center">

# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

[Contributing Guidelines](./CONTRIBUTING.md) · [Request a Feature]({{ cookiecutter.project_url }}/-/issues/new?issuable_template=Feature) · [Report a Bug]({{ cookiecutter.project_url }}/-/issues/new?issuable_template=Bug)

</div>

## Usage

This application is released as a Docker image. You can run it with:

```bash
$ docker run -it registry.gitlab.com/{{ cookiecutter.project_url.lstrip("https://gitlab.com/") }}:{{ cookiecutter.version }}
```

## Development

To run the bot locally, clone this repo and follow the instructions:

```bash
$ make env-compile
$ make env-create
```

This will create a virtual environment with all the needed dependencies (using [tox](https://tox.readthedocs.io/en/latest/)). You can activate this environment with:

```bash
$ source ./.tox/{{cookiecutter.project_slug}}/bin/activate
```

Then, you can run `make help` to learn more about the different tasks you can perform on the project using [make](https://www.gnu.org/software/make/).

But back to what we are interested in, to run the bot, you must follow the following steps:

1. Create a bot using father bot and getting its apikey. [Here](https://core.telegram.org/bots#how-do-i-create-a-bot) you will find more information.
1. Add the Telegram bot API key to your `.bashrc` / `.zshrc` ...
    ```bash
    export BOT_APIKEY='your-API-key-here'
    ```
3. Run the bot
    ```bash
    make run
    ```
And that's it! Your bot is running an ready to start a conversation. Try to send `/start` or `/help` commands in your telegram bot and you should get a response message!

## License

[Copyright](./LICENSE)