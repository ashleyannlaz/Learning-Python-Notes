# Example file for variables
f = 0
print(f)
# Re declaring the variable
f = "abc"
print(f)
# Cannot concatenate str and int objects
# print('this is a string' + 123)
print('this is a string ' + str(123))

# Global vs local variables in functions
# Python does have local variables
def someFunction():
    global f
    # declares f as global
    f="def"
    print(f)

someFunction()
print(f)

del f
# deletes the variable
print(f)