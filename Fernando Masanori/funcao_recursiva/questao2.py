# def f(n):
#     if n == 1: return 1
#     return 2 * f(n - 1)

# print(f(80))

from functools import cache

@cache

def f(n):
    if n == 1: return 1
    return f(n - 1) + f(n - 1)

print(f(80))