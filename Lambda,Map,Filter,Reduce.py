#Lambda

add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y

print('The answer is:', add(3, 4))
print('The answer is:',sub(10, 6))
print('The answer is:',mul(10, 10))
print('The answer is:',div(100, 5))

square = lambda n: n * n
cube = lambda n: n * n * n
print('The answer is:',square(3))
print('The answer is:',cube(4))

#Map

Vegetables = ['carrot', 'cabbage', 'beetroot', 'beans']
result = list (map(lambda Vegetable: Vegetable.capitalize(), Vegetables))
print ('After capitalizing:', result)

result = list(map(lambda Vegetable: Vegetable.upper(), Vegetables))
print('After upper:', result)

result = list(map(lambda Vegetable: Vegetable.lower(), Vegetables))

#Filter

numb = [1,2,3,4,5,6]
even = list(filter(lambda x: x % 2 == 0, numb))
print('Even:', even)

#Reduce
from functools import reduce
nums = [1,2,3,4]
print(reduce(lambda a,b: a+b, nums))