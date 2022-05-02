def my_function():
    print("I have been called!!!")

def is_odd(n):
    # we can make use of the modulo operator (checks the remainder of a division) to 
    # detect if a number is odd. 
    # if it is even, return True
    # otherwise return False.
    print("number is even") if n % 2 == 0 else print("number is odd")

# if we don't pass an argument to this function, it will assume
# the default value for n, which is 10
def fn_with_default(n = 10):
    return n + 2

# *args takes a variable number of arguments
def fn_args(*args):
    print("function with args, *args is: ")
    print(args)

# **kwargs takes a variable number of named arguments
def fn_kwargs(**kwargs):
    print("function with kwargs, **kwargs is: ")
    print(kwargs)

my_function()
is_odd(6)
is_odd(5)
fn_with_default()
fn_args(1, 2, 3)
fn_kwargs(a = 1, b = 2, c = 3)
