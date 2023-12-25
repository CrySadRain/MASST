def remove_duplicates(nums):
    if not nums:
        return 0

    last_unique_index = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[last_unique_index]:
            last_unique_index += 1
            nums[last_unique_index] = nums[i]

    return last_unique_index + 1, nums[:last_unique_index + 1]

user_input = input("Введіть масив: ")
nums = list(map(int, user_input.split()))

result, unique_nums = remove_duplicates(nums)
unique_nums.sort()
print("k =", result, unique_nums)