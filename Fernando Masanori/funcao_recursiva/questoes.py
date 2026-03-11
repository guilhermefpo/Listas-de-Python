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

# 