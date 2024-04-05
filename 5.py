a = int(input())
for b in range(0, a+1):
    b += 1
    if b**3 < a:
        print(b**3, end=" ")


