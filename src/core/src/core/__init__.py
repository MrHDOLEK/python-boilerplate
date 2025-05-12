from utils import return_one


def hello():
    print("Hello from core core!")


def return_two() -> int:
    return 1 + return_one()
