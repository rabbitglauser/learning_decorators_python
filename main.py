from functools import wraps
from time import perf_counter, sleep


def get_time(func):
    """times any function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)  # Store function result
        end_time = perf_counter()
        total_time = round(end_time - start_time, 2)  # Correct round application
        print('Time', total_time, 'seconds')
        return result  # Return function result

    return wrapper  # Correct return position


@get_time
def do_something(param: str):
    """Does something important"""
    sleep(1)
    print(param)


if __name__ == '__main__':
    do_something('hello')
