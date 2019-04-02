##########
# Strings
##########
my_string = 'abcdefg'
split_string = "Nishant Chutiya"
split_string2 = "Hello World"

# Basics

'hello'
"hello"
"I'm a dog"

# Indexing
# indexing starts from 0

print(my_string)
print(my_string[0])
print(my_string[-1])
print(my_string[3])

# Slicing
# 3 steps : beginning of the slice, end of the slice, step of the slice

print(my_string[2:]) # From index 2 to all the way to the end of string
print(my_string[4:])

print(my_string[:3]) # upto from start but excluding the index 3

print(my_string[2:5]) # from index upto index

print(my_string[:]) # print all

print(my_string[::2]) # all the way from beginnig to end with step size 2

print(my_string[1:6:2]) # from index 1 to 6 with step size 2

# strings are immutable
# my_string[1] = 'R' << wrong

# Basic Methods
# make all letter uppercase

x = my_string.upper()
print(x)

# make all letter lowercase
y = my_string.lower()
print(y)

# make the first letter uppercase hence capitalize
z = my_string.capitalize()
print(z)

# splits words in a string (i.e sentence) separated by a white space by default
split_01 = my_string.split()
print(split_01)

# splits words in a string (i.e sentence) separated by a white space by default
split_02 = split_string.split()
print(split_02)

# split at specified character, here 'd'
split_03 = my_string.split('d')
print(split_03)

# split at specified character, here 'n'
split_04 = split_string.split('n')
print(split_04)

# split at specified character, here 'o'
split_04 = split_string2.split('o')
print(split_04)

# Extract Splitted Strings
tweet = "Go Sports! #Sports"
tweet_result = tweet.split('#')[1]
print(tweet_result)

# Print Formatting

print_formatting_01 = "Insert another string here: {}".format("INSERT ME!") # Insert one string in another
print(print_formatting_01)

question = "Chutiya Kaun Hey ?"
answer = "Nishant Hunter !"

print_formatting_02 = "[Q]: {}\n[A]: {}".format(question,answer)
print(print_formatting_02)

print_formatting_03 = "Ek tha {x},  Ek thi {y}".format(x = "gamer", y="doctor")
print(print_formatting_03)