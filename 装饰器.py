def PrintHello(func):
    def _():
        func()
        print(2)

    return _


@PrintHello
def hello() -> None:
    print(1)


hello()
