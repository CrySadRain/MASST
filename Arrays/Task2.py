def count_numbers_with_even_digits(nums):
    def count_digits(num):
        count = 0
        while num > 0:
            num //= 10
            count += 1
        return count

    result = 0
    for num in nums:
        if count_digits(num) % 2 == 0:
            result += 1

    return result

nums = list(map(int, input("Введіть числа: ").split()))

output = count_numbers_with_even_digits(nums)

print(f"Кількість чисел з парною кількістю цифр: {output}")