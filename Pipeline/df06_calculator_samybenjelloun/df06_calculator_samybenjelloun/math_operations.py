def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(arg1: float, arg2: float) -> float:
    if arg2 == 0:
        raise ZeroDivisionError("arg2 cannot be 0, since you cannot divide by 0")
    return arg1 / arg2

