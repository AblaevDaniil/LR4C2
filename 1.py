#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
from functools import lru_cache


def factorial(n = 10):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def fib(n = 10):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


@lru_cache
def factorial1(n = 10):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


@lru_cache
def fib1(n = 10):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


if __name__ == '__main__':
    start_time = timeit.default_timer()

    factorial(900)
    print("Факториал без @lru_cache длится:", timeit.default_timer() - start_time, "секунд")

    start_time = timeit.default_timer()

    factorial1(900)
    print("Факториал с @lru_cache длится:", timeit.default_timer() - start_time, "секунд")

    start_time = timeit.default_timer()

    fib(30)
    print("Фиббоначи без @lru_cache длится:", timeit.default_timer() - start_time, "секунд")

    start_time = timeit.default_timer()

    fib1(30)
    print("Фиббоначи с @lru_cache длится:", timeit.default_timer() - start_time, "секунд")