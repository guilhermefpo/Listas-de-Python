
# Inverte str

def inv(s):
    if len(s) == 0: return " "
    ultimo = s[-1:]
    str_sem_ultimo = s[0:-1]
    return ultimo + inv(str_sem_ultimo)

print(inv("Abacate"))

# 2º mdc
def mdc(a, b):
    if a % b == 0: return b
    return mdc(b, a % b) 


print(mdc(5, 10))

# sd
def sd(n):
    if n <= 9: return n
    return sd(n//10) + n % 10

print(sd(123)) 

# dec2bin
def dec2bin(n):
    if n == 0: return ''
    return dec2bin(n // 2) + str(n % 2)

print(dec2bin(18))


# fib
# dic = {}
# def fib(n):
#     if n == 1 or n == 2: return 1
#     if n not in dic: dic[n] = fib(n - 1) + fib(n - 2)
#     return dic[n]
# print(fib(100))

from functools import cache

@cache

def fib(n):
    if n == 1 or n == 2: return 1
    return fib(n - 1) + fib(n - 2)
print(fib(100))

