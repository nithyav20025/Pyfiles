def get_numbers(n):
    return [i for i in range(n)]

print(get_numbers(15))


def get_numbers(n):
    for i in range(n):
        yield i

for num in get_numbers(15):
    print(num)

print(get_numbers(15))
