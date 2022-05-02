# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 12:14:52 2022

"""

"""
Question 2: it is important to make a custom class iterable to go through
its components. For example, we might store a custom list of custom objects inside
a class, and by default this list won't be iterable, that's why it's important
to make a custom class iterable. But it also depends on the use case.
"""

# Question 1
class FibonacciBase():
    def __init__(self, m):
        self.max = m

# Question 4
class FibonacciBase2(FibonacciBase):
    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

# Question 5
class Fibonacci(FibonacciBase2):
    def __next__(self):
        x = self.a
        if x > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        
        return x

print()
print("Questions 3, 3a, 3b, 6")
# Questions 3, 3a and 3b
fib = Fibonacci(100)
print(iter(fib))
# Question 6
for i in fib:
    print(i)
# if the class isn't iterable it throws an error
# > TypeError: "FibonacciBase" object is not iterable

print()
print("Question 7")
# Question 7
print("Iterating using for")
l = [x for x in fib]
for i in l:
    print(i)

print()
print("Iterating using while")
i = 0
while i < len(l):
    print(l[i])
    i += 1