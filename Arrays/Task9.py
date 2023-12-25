def replace_elements(arr):
    n = len(arr)
    
    max_right = arr[n - 1]
    
    arr[n - 1] = -1
    
    for i in range(n - 2, -1, -1):
        temp = arr[i]
        
        arr[i] = max_right
        
        max_right = max(max_right, temp)
    
    return arr

arr_input = input("Введіть масив: ")
arr = list(map(int, arr_input.split()))

result = replace_elements(arr)
print("Результат:", result)