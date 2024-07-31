def bpower(a, n):
    pow = 1
    for i in range(n):
        pow *= a
    return pow

def dpower(x, y):
    if y == 0:
        return 1
    temp = dpower(x, y // 2)
    if y % 2 == 0:
        return temp * temp
    else:
        return x * temp * temp
#
a = int(input("Enter a: "))
n = int(input("Enter n: "))
print("Brute Force method a^n: ", bpower(a, n))
print("Divide and Conquer a^n: ", dpower(a, n))
