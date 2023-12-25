def count_repeats(nums):
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 0

    max_count = max(max_count, current_count)

    return max_count

def input_array():
    try:
        input_string = input("Введіть бінарний масив: ")
        nums = list(map(int, input_string.split()))

        if all(num == 0 or num == 1 for num in nums):
            return nums
        else:
            print("Помилка: Масив повинен містити тільки числа 0 або 1.")
            return None

    except ValueError:
        print("Помилка: Неправильний формат введеного рядка.")
        return None

nums = input_array()

if nums:
    print("Введений масив:", nums)

    result = count_repeats(nums)
    print("Максимальна кількість повторень: ", result)