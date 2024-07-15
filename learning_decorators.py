import time


def tictoc(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func()
        t2 = time.time()
        print(f"{func.__name__} took {t2 - t1} seconds")
    return wrapper


@tictoc
def do_this():

    time.sleep(1.3)


@tictoc
def do_that():
    time.sleep(.4)


do_this()
do_that()
print('Done')
