#functions that return an object that can be iterated over
import sys
def thegenerator():
    yield 1
    yield 2
    yield 3
g = thegenerator()
print(sum(g))
sorted(g)

def countdown(num):
    print('Starting')
    while num > 0:
        yield num 
        num -= 1
cd = countdown(9)
value = next(cd)
print(value)
value = next(cd)
print(next(cd))
def firstn(n):
    nums = []
    num = 0
    while nums < n:
        nums.append(num)
        num += 1
        return nums
def firstn_generator(n):
    num = 0
    while num < n:
        yield num 
        num += 1
print(sys.getsizeof(firstn(1000000)))
print(sys.getsizeof(firstn_generator(1000000)))
def fibonacci(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a,b = a+b
fib = fibonacci(30)
for i in fib:
    print(i)
generator = (i for i in range(10) if i % 2 == 0)
for i in generator:
    print(i)



 