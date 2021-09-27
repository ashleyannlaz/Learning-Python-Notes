# Python Functions

# Define basic function
def func1():
    print('I am a function')

# PRINT FUNCTIONS
# func1()
# print(func1())
# # functions are objects
# print(func1)
# --------------------------------

# Function that takes arguments
def func2(arg1, arg2):
    print(arg1, "", arg2)

# func2(10,20)
# print(func2(10,20))
# --------------------------------

# Function that returns a value
def cube(x):
    return x*x*x

# cube(3)
# print(cube(3))

# --------------------------------

# Function with default value for an argument
def power(num, x = 1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# print(power(2))
# print(power(2,3))
# You can input args in the opposite
# print(power(x=3, num=2))

# function with variable number or args
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print(multi_add(1,1,2))

