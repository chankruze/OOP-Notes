#########
#  Lists
#########
list_01 = [1,2,3]
list_02 = ['abcdefg',1,2,12.4,True,'asdf',[1,2,False,'string']]
list_other = ['x','y','z']
print(list_02)
print(len(list_02))

# indexing
print(list_01[0])
print(list_02[3:7])

# mutable
print("Before Reassignment :",list_01)
list_01[0] = "I'm reassigned !"
print("After Reassignment :" ,list_01)

# basic methods
# append elements at last index
list_01.append("New Item")
print(list_01)
list_01.append(list_other)
print(list_01)

# extend the list by adding elements
list_01.extend(list_other)
print(list_01)

# remove
popped_item = list_01.pop()
print(list_01)
print(popped_item)

popped_item_01 = list_01.pop(0)
print(list_01)
print(popped_item_01)

# reverse
list_01.reverse()
print(list_01)

# sort
sort_list = [4,6,2,3,8,1,2,30.0122,1.5,5,2,0]
sort_list.sort()
print(sort_list)

# nested list
nested_list = [1,2,['x','y','z']]
print(nested_list[2][1])

# list comprehension
matrix = [[1,2,3,4],[5,6,7],[8,9,0]]

first_col = [row[0] for row in matrix]
print(first_col)