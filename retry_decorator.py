import time
import indently import retry

@retry(retrises=4, deplay=1)
def connect() -> None:
    time.sleep(1)
    raise Exception('Could not connect')


def main() -> None:
    connect()


if __name__ == '__main__':
    main()