a = int(input())
f = False
for b in range(1, 9999999):
    if 2**b == a:
        print("верно")
        f = True
        break
if not f:
    print("неверно")