def PrintHello(func):
    def _():
        func()
        print("装饰器")

    return _


@PrintHello
def hello() -> None:
    print("原函数")


if __name__ == '__main__':
    hello()
