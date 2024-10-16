from typing import Optional

import typer

from typing_extensions import Annotated


app = typer.Typer(help='sample cli')


@app.callback()
def cb(
    ctx: typer.Context,
    opt0: Annotated[str, typer.Option(help='a global option')] = 'hello'
) -> None:
    # This always runs, regardless of the sub-command.
    ctx.obj = {'greeting': opt0}


@app.command()
def cmd1(
    ctx: typer.Context,
    arg1: Annotated[str, typer.Argument(help='a required argument')]
) -> None:
    # This command takes a required string argument and prints it.
    print(f'{ctx.obj["greeting"]}, {arg1}.')


@app.command()
def cmd2(
    opt2: Annotated[Optional[int], typer.Option(help='a required option')] = None
) -> None:
    # This command takes an optional integer option and prints it.
    # If the option is not provided, it defaults to None.
    print(opt2)


def main() -> None:  # pragma: no cover
    app()


if __name__ == '__main__':  # pragma: no cover
    main()
