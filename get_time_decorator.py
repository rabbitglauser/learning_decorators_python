import time
from indently import get_time


def connect() -> None:
    print("Connecting...")
    time.sleep(2)
    print("Connected!")


def fifty_million_loops() -> None:
    fifty_million_loops: int = int(5e7)


    print('Looping...')
    for _ in range(fifty_million_loops):
        pass

    print('Done looping!')


def mian() -> None:
    connect()
    fifty_million_loops()


if __name__ == '__main__':
    get_time_decorator()