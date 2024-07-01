https://python-poetry.org/docs/cli/

% python-collab-template % curl -sSL https://install.python-poetry.org | python3 -
% poetry config virtualenvs.in-project true

% poetry add <library> [--group dev]
% poetry remove <library> [--group dev]

# We could make dev "required" and drop it in prod via "--without dev",
# or via "--only prod".
% poetry install --with dev | poetry update
% poetry shell
% python src/cli.py --help

Retrieving Poetry metadata

# Welcome to Poetry!

This will download and install the latest version of Poetry,
a dependency and package manager for Python.

It will add the `poetry` command to Poetry's bin directory, located at:

/Users/cbornman/.local/bin

You can uninstall at any time by executing this script with the --uninstall option,
and these changes will be reverted.

Installing Poetry (1.8.3): Done

Poetry (1.8.3) is installed now. Great!

To get started you need Poetry's bin directory (/Users/cbornman/.local/bin) in your `PATH`
environment variable.

Add `export PATH="/Users/cbornman/.local/bin:$PATH"` to your shell configuration file.

Alternatively, you can call Poetry explicitly with `/Users/cbornman/.local/bin/poetry`.

You can test that everything is set up by executing:

`poetry --version`


