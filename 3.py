n = int(input(":"))
while int(n**0.5)*int(n**0.5) != n:
    print("не является полным квадратом")
    n = int(input(":"))
if int(n**0.5)*int(n**0.5) == n:
    print("это полный квадрат")