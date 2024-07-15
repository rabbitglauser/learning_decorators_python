from functools import wraps
from time import perf_counter , sleep


def do_something(param: str):
    """Does something important"""

    sleep(1)
    print(param)


if __name__ == '__main__':
    do_something('hello')
