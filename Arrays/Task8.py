def mountain_array(arr):
    n = len(arr)
    
    if n < 3:
        return False
    
    peak_index = arr.index(max(arr))
    
    if peak_index == 0 or peak_index == n - 1:
        return False

    for i in range(peak_index):
        if arr[i] >= arr[i + 1]:
            return False
    
    for i in range(peak_index, n - 1):
        if arr[i] <= arr[i + 1]:
            return False
    
    return True

arr_input = input("Введіть масив цілих чисел: ")
arr = list(map(int, arr_input.split()))

result = mountain_array(arr)
print(f"Чи є введений масив гірським: {result}")