# 14495 v
def fibo(x):
    if x == 1 or x == 2 or x == 3:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fibo(x - 1) + fibo(x - 3)
    return d[x]


n = int(input())
d = [0] * (n+4)
print(fibo(n))
