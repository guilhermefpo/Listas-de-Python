def fat(n):
    if n <= 1: return 1
    return n * fat(n - 1)

print(fat(3))

# if 3 <= 1:
# return 3 * fat(2)

# if 2 <= 1:
# return 2 * fat(1)

# if 1 <= 1: return 1

def pot(x, n):
    if n == 0: return 1
    return x * pot(x, n - 1)

print(pot(2, 3))

# if 3 == 0: return 1
# return 2 * pot(2, 2)

# if 2 == 0: return 1
# return 2 * pot(2, 1) # acorda 2 * 4 == 8

# if 1 == 0: return 1
# return 2 * pot(2, 0) # acorda 2 * 2 == 4

# if 0 == 0: return 1 # acorda 2 * 1 == 2

