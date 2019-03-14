########################
# COMPARISON OPERATORS #
########################

# Greater than
1 > 2

# Less than
1 < 2

# Greater than or Equal to
1 >= 1

# Less than or Equal to
1 <= 4

# Equality
1 == 1          #True
1 == "1"        #False
'hi' == 'bye'   #False

# Inequality
1 != 2          #True

#####################
# LOGICAL OPERATORS #
#####################

# AND
(1 >2) and (2 < 3)

# OR
(1 > 2) or (2 < 3)

# Multiple logical operators
(1 == 2) or (2 == 3) or (4 == 4)

# In
print('x' in [1,2,3,'x'])

my_list_02 = [1,3,4,5,6,'Hello',10,True]
print(2 in my_list_02)

# IF

if 1 < 2:
    print('yes')

if 1 < 2:
    print('First Block')
    if 20 < 3:
        print('Second Block')

# IF ELSE

if 1 < 2:
    print("If satisfied")
else:
    print("Else satisfied")

# IF ELIF ELSE

if 1 > 2:
    print("Hello")
elif 3 == 3:
    print("elif ran")
else:
    print('last')

#########
# LOOPS #
#########

# For Loops

seq = [1,2,3,4,5,6]

for jelly in seq:
    # Code here
    print(jelly)

dict = {'sam':1, 'Frank':2, 'Dan':3}

# simple for loop itteration on a dictionary just prints the keys not values
for item in dict:
    print(item)

# ittrate the keys with values of a dictionary
for k in dict:
    print(k,':',dict[k])

# Itterating thru tuples
my_pairs = [(1,2),(3,4),(5,6)]

for tups in my_pairs:
    print(tups)

# tuple unpacking
# if the tuples are in a seqence we can unpack them
for tup1,tup2 in my_pairs:
    print(tup1)
    print(tup2)


# While Loops

i = 1

while i < 5:
    print("i is: {}".format(i))
    i += 1

# Range function
# Range instance (generates list without saving to computer, it saves and ittrates in memory)
range_01 = range(100000)
print(range_01)

# Range with 2 params (starting point, ending point(excluded)). By default step size is 1
range_02 = list(range(0,5))
print(range_02)

# Range with 3 params (starting point, ending point(excluded), step size)
range_03 = list(range(0,101,10))
print(range_03)

# for loop with range
for item in range(10):
    print(item)

# List Comprehension Continued
list_x = [1,2,3,4]

out_01 = []
for num in list_x:
    out_01.append(num**2)

print(out_01)

# or

out_02 = [num**2 for num in list_x]
print(out_02)