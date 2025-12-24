def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by 0"

print(divide(100, 4))


