def check_double(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n):
            if i != j and arr[i] == 2 * arr[j]:
                return True

    return False

arr_example = list(map(int, input("Введіть елементи масиву: ").split()))

result = check_double(arr_example)
print(result)
