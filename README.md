# Cookiecutter Python Telegram Bot

A [cookiecutter](https://github.com/audreyr/cookiecutter) template for Python Telegram Bot (ready for CI/CD pipelines) based on [python-template](https://github.com/clarriu97/python-template) and [virus/total-telegram-bot](https://github.com/clarriu97/virus-total-telegram-bot), repos of my college [clarriu97](https://github.com/clarriu97).

## Features

* **Scripted operations**: with [GNU make](https://www.gnu.org/software/make/)
* **Testing**: with [pytest](https://docs.pytest.org/en/latest/)
* **Multiple Python versions support**: Setup [tox](https://tox.readthedocs.io/en/latest/) to easily test for Python 3.8, 3.9, etc.
* **Package documentation**: ready for generation with [mkdocs](https://www.mkdocs.org/)
* **Version handling**: Pre-configured version bumping with a single command: [bump2version](https://pypi.org/project/bump2version/)

## Quickstart

[Install cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html) (1.4.0 or higher):

```bash
python3 -m pip install --user cookiecutter
```

Create the project:

```bash
cookiecutter https://github.com/clarriu97/python-template
```

Fill all the details and your project should be ready in a matter of seconds!

If you want to upload your project to Github, please make sure the URL is the same as the one you configured during project creation to ensure everything works properly (links, etc.).

## Configuration

The template provides sensible defaults for all the configuration options, however you can customize your project using the following parameters:

* `author`: The name of the person or team behind this project.
* `author_email`: The email of the author. In the case of a team or group, you can use a mailing list address.
* `project_name`: The name of the project. Prefer short names (ideally one word) using [kebab-case](https://en.wikipedia.org/wiki/Letter_case#Special_case_styles) (hyphen-separated lowercase letters)
* `project_slug`: The name of the project in [snake case](https://en.wikipedia.org/wiki/Snake_case)  (underscore-separated lowercase letters). Will be autogenerated if left empty.
* `project_short_description`: A short description of the project
* `project_url`: The Github URL of the project. It's recommended that you create the project first on Github and paste the generated URL here.
* `version`: The initial version ([Semantic Versioning](https://semver.org/)). It's recommended you use the default value (`0.1.0`).
* `python_versions`: The supported python versions. If possible, prefer supporting only the latest version available.

## Contributing

You can freely contribute to this template by submitting a merge request with the intended changes. Before you do, please take a look at the [CONTRIBUTING](./CONTRIBUTING.md) guidelines.

## Request a Feature / Fork This / Create Your Own

If you have differences in your preferred setup, you are encouraged to fork this or create your own template. But before you do, please contact the maintainers of this repo to see if the missing feature can be added (or do it yourself!). The recommended way is to create an issue detailing what the feature is and the value it would bring.