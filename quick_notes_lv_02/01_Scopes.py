# Python scope follows the LEGB rule:
#   -> Local
#   -> Enclosing Function locals
#   -> Global
#   -> Built-in
#
# L: Local - Names assigned in any way within a function (def or lambda), and not declared global in that function
# E: (EFLs) - Name in the localscope of any all enclosing functions (def or lambda), from inner to outer
# G: Global (module) - Names assigned at the top-level of a module file, or declared globa; in adef within the file.
# B: Built-in (Python) - Names preassigned in the built-in names module (open, range, SyntaxError, len, .. etc.)
#####################################################################################################################

# Global
x = 25

# Built-in
# Never reassign built-in vars in global scope

# Local
lambda x: x**2

def my_func():
    x = 50
    return x

print(x) # global x
print(my_func()) # local x

my_func() # no effect on global
print(x) # still global x

# Enclosing function level
name = "Toby" # This is a global name !

def greet():
    name = "Sammy" # got first hit on 'name' so hello() will use this
    # If above line is commented, it will search up and use Toby

    def hello():
        # no variable named name in helllo() so it will search up in greet()
        print("Hello " + name)
    hello()

greet() # use local var
print(name) # outside function, global will be used

y = 50

def func(y):
    print('y is :', y)
    y = 1000
    print("local y changed to :", y)

func(y)
print(y)

# Rename global variables inside a function
def global_func():
    global y
    y = 999

print("before function call, y is : ", y) # unaffected global var
global_func() # reassigns global var
print("after function call, y is : ", y) # global var changed with global keyword

# How to do the same but avoid using global ?
z = 50

def func_z():
    # global z
    z = 4444
    return z

print("before function call, z is : ", z) # unaffected global var
z = func_z() # reassigns global var
print("after function call, z is : ", z) # global var changed without global keyword