def sorted_squares(nums):
    result = [x**2 for x in nums]
    result.sort()
    return result

nums_input = input("Введіть масив цілих чисел: ")
nums = list(map(int, nums_input.split()))

sorted_nums = sorted(nums)

print("Відсортований вихідний масив:", sorted_nums)

result = sorted_squares(sorted(nums))

print("Відсортовані квадрати чисел:", result)