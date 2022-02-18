from functools import lru_cache

@lru_cache(maxsize=1000)
def f(n):
    if n <= 13: