import uvicorn

from app import create_app


app = create_app()


if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host='0.0.0.0',
        port=8001,
        debug=False,
        reload=True,
    )

    # import typer
    #
    # app = typer.Typer()
    #
    #
    # @app.command()
    # def hello(name: str):
    #     typer.echo(f"Hello {name}")
    #
    #
    # @app.command()
    # def goodbye(name: str, formal: bool = False):
    #     if formal:
    #         typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    #     else:
    #         typer.echo(f"Bye {name}!")


