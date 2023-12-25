def reverse_string(s):
    if len(s) == 0:
        return s

    print(s[-1], end='')
    reverse_string(s[:-1])

input_string = input("Введіть строку: ")
print("Введена строка:", input_string)
print("Реверсивна строка:", end='')
reverse_string(input_string)