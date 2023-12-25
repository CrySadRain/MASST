def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Input: n = "))
result = fibonacci(n)
print(f"Output: {result}")
print(f"Explanation: F({n}) = F({n - 1}) + F({n - 2}) = {result}")