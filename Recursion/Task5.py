def my_pow(x, n):
    if n == 0:
        return 1.0
    if n < 0:
        x = 1 / x
        n = -n
    return x ** n

x = float(input("Введіть значення x: "))
n = int(input("Введіть значення n: "))

result = my_pow(x, n)
print(f"Input: x = {x}, n = {n}")
print(f"Output: {result}")