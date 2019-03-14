######################
## -- Problem 01 -- ##
######################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appers in the list somewhere

# For example:

# array_check([1, 1, 2, 3, 1]) -> True
# array_check([1, 1, 2, 4, 1]) -> True
# array_check([1, 1, 2, 1, 2, 3]) -> True

def array_check(nums):
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+2] and nums[i+2] == 3:
            return True
    return False

######################
## -- Problem 02 -- ##
######################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# string_bits('Hello') -> 'Hlo'
# string_bits('Hi') -> 'H'
# string_bits('Heeololeo') -> 'Hello'

def string_bits(string):
    new_string = ""
    for i in range(len(string)):
        if i%2 == 0:
            new_string = new_string + string[i]
    return new_string

# OR

def string_bits2(string):
    new_string = string[::2]
    return new_string

######################
## -- Problem 03 -- ##
######################

# Given 2 strings, return True if either of the strings appears at very end
# of the other string, ignoring upper/lower case differences
# computation shouldn't be "case sensitive"

# For Example:

# end_other("Hiabc", "abc") -> True
# end_other("AbC", "HiaBc") -> True
# end_other("abc", "abXabc") -> True

def end_other(str1, str2):
    str1 = str1.lower
    str2 = str2.lower
    return (str2.endswith(str1) or str1.endswith(str2))
    
# OR

def end_other2(str1, str2):
    str1 = str1.lower
    str2 = str2.lower

    return str1[-(len(str2)):] == str2 or str2[-(len(str1))] == str1

######################
## -- Problem 04 -- ##
######################

# Given a string, return a string where for every char in the original,
# there are two chars.

# For Example:

# double_char("The") -> "TThhee"
# double_char("AAbb") -> "AAAAbbbb"
# double_char("Hi-There") -> "HHii--TThheerree"

def double_char(string):
    result = ""
    for char in string:
        result += char*2
    return result

######################
## -- Problem 05 -- ##
######################

# Read this problem statement carefully !

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value ounts as 0, except 15 and
# 16 don't count as a  teens. Write a separate helper "def fix_teen(n):" that takes
# in an int value and returns that value fixed for the teen rule.

# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and the same indent level as the main no_teen_sum().
# Again, you will have 2 functions for this problem !

# For Example:

# no_teen_sum(1, 2, 3) -> 6
# no_teen_sum(2, 13, 1) -> 3
# no_teen_sum(2, 1, 14) -> 3

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    if n [13,14,17,18,19]:
        return 0
    return n

######################
## -- Problem 06 -- ##
######################

# Return the number of even integers in the given array.

# For Example:

# count_evens([2, 1, 2, 3, 4]) -> 3
# count_evens([2, 2, 0]) -> 3
# count_evens([1, 3, 5]) -> 0

def count_evens(check_array):
    count = 0

    for elem in check_array:
        if elem % 2 == 0:
            count += 1
    return count

# OR

def count_evens2(check_array):
    even_nums_array = filter(lambda even_num: even_num % 2 == 0, check_array)
    even_nums_count = len(list(even_nums_array))
    return even_nums_count