###############
# Dictionaries
###############
# No order only key value pairs

my_stuff = {"key1":"value1","key2":"value2", "key3" : {'nk1' : [1,2,3,'grab me !']}}
print(my_stuff['key2'])

# Grab a particular item (try solving  [inside] - [out])
print(my_stuff['key3']['nk1'][3])
print(my_stuff['key3']['nk1'][3].upper())

# Reassign dictionary items
my_food = {'lunch' : 'pizza', 'bfast' : 'eggs', 'dinner' : 'chicken'}
my_food['lunch'] = 'Ham Burger'
my_food['dinner'] = 'Pasta'
print(my_food['lunch'])
print(my_food)