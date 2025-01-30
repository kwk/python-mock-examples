def hello() -> str:
    return "Hello"


def greet(name: str) -> str:
    return f"{hello()}, {name}"


def helloWithArg(name: str = "") -> str:
    return f"Hello, {name}"


def greetWithArg(name: str) -> str:
    return helloWithArg(name)


class HelloAndBye:
    def __init__(self):
        pass

    def hello(self, name: str) -> str:
        return f"Hello, {name}!"

    def bye(self, name: str) -> str:
        return f"Bye, {name}!"


class Greeter:
    def __init__(self, hello: HelloAndBye):
        self.hello_obj = hello

    def say_hello(self, name: str) -> str:
        return self.hello_obj.hello(name)

    def say_bye(self, name: str) -> str:
        return self.hello_obj.bye(name)
