import time
from functools import cache


@cache
def count_vowels(text: str) -> int:
    vowels_count = 0
    print(f'Bot: Counting vowels in: "{text}"...')
    time.sleep(2)
    for letter in text:
        if letter in "aeiou":
            vowels_count += 1
    return vowels_count


def cache_decorator():
    print(count_vowels("Hello World"))
    print(count_vowels("Hello World"))
    print(count_vowels('Samuel'))
    print(count_vowels.cache_info())
    print(count_vowels.cache_parameters())
    count_vowels.cache_clear()


if __name__ == '__main__':
    cache_decorator()
