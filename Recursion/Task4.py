def count_ways(n):
    if n <= 1:
        return 1
    return count_ways(n - 1) + count_ways(n - 2)

def print_climbing_ways(n):
    if 1 <= n <= 45:
        ways = count_ways(n)
        print(f"Введення: n = {n}")
        print(f"Вивід: {ways}")
        print("Пояснення: Є наступні способи піднятися нагору:")
        print_ways_recursive(n, [])
    else:
        print("Помилка: n повинно бути у межах від 1 до 45")

def print_ways_recursive(remaining, path):
    if remaining == 0:
        print(" ".join(map(str, path)))
    elif remaining > 0:
        print_ways_recursive(remaining - 1, path + [1])
        print_ways_recursive(remaining - 2, path + [2])

n = int(input("Введіть кількість сходинок (n): "))
print_climbing_ways(n)
