def hello() -> str:
    return "Hello"


def greet(name: str) -> str:
    return f"{hello()}, {name}"


def helloWithArg(name: str = "") -> str:
    return f"Hello, {name}"


def greetWithArg(name: str) -> str:
    return helloWithArg(name)
