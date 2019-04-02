############
#  Booleans
############
True
False
1
0

#########
# Tuples
#########
# Tuples are immutable sequences

tuple = (1,2,3)
print(tuple[0])

tuple = ('a', True, 123)
print(tuple)

# tuple[0] = 'New' (wrong)
print(tuple)

#########
#  Sets
#########
x = set()

x.add(1)
x.add(2)
x.add(1.5)
x.add(4)
print(x)

# elements are unique
x.add(4)
x.add(4)
x.add(4)
x.add(4)
print(x)

# set call on a list which has elements repeated
converted = set([1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,5,5,5,5,4,4,0])
print(converted) 