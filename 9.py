n, k, r = map(int, input().split())
a = 1
while r > n:
    a += 1
    n *= (1+(k/100))
print(a)