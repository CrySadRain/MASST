def sort_array(nums):
    nums.sort(key=lambda x: x % 2)
    return nums

nums = list(map(int, input("Введіть масив: ").split()))

result = sort_array(nums)
print(result)