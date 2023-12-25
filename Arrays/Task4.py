def duplicate(arr):
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop()
            i += 2
        else:
            i += 1

arr = list(map(int, input("Введіть масив цілих чисел: ").split()))

duplicate(arr)

print("Результат:", arr)