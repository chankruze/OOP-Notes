#############
# FUNCTIONS #
#############

# Basic function
def my_function_01(param = 'default'):
    print("My Function Executed !")

my_function_01()

# Function with a Docstring
def my_function_02(param1 = 'It Works !'):
    """
    THIS IS THE DOCSTRING
    """
    print("My Function Executed And {}".format(param1))

my_function_02('Param1 Changed !')

# Return statement
def hello():
    return "Hello !"

result = hello()
print(result)

# If we are not strict about data type in python terrible things will happen like below example.
def addNum(num1, num2):
    return num1 + num2

result2 = addNum('2', '3')
print(result2)

# So we need to check data type of our parameters
def sum(num1, num2):
    """
    # params : num1, num2
    # usage : sum(10,20) 

    Adds two integers (num1, num2) and returns their sum.
    """
    if type(num1) == type(num2) == type(10):
        return num1 + num2
    else:
        return "Sorry, I need integers !"

result3 = sum('23',90)
print(result3)

result4 = sum('23','90')
print(result4)

result5 = sum(23,90)
print(result5)

# Filter
mylist = [1,2,3,4,5,6,7,8]

def is_even(num):
    return num % 2 == 0

evens = filter(is_even, mylist)
print(list(evens))

##########################################
# Lambda Expression (Anonymous Function) #
##########################################
# If we are using a function only once in our program, we can use a lambda expression a.k.a anonymous function
# Above is_even function is re written in lambda expression

even_nums = filter(lambda num: num % 2 == 0, mylist)
print(list(even_nums))
