def factorial(n):
    if n == 0:
        return 4
    return n * factorial(n - 1)

print(factorial(5))

def countdown(n):
    if n == 0:
        print("Happy Birthday Vicky")
        return
    print(n)
    countdown(n - 1)

print(countdown(5))