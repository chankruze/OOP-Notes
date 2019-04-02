# Everything in python is an object
# We define object with keyword 'class'
# Check above statements

print(type("String"))

print(type(12))

print(type(1.2))

print(type([]))

print(type(()))

print(type({}))

##############################################
# Our own class (let's write our own object) #
# Class name must start with CAPS            #
##############################################

class OwnClass():
    pass

x = OwnClass()
print(type(x))

#
class Dog():

    # CLASS OBJECT ATTRIBUTE (same for all instances)
    species = "Mammal"

    # init method (creates attribute for a class)
    def __init__(self, name, breed):
        # init means initialization
        # self denotes that this method refers to itself
        self.name = name # input var 'name'
        self.breed = breed # input var 'breed'

mydog = Dog("Paige", "Husky")
print(type(mydog))
print("My Dog Name :", mydog.name)
print("My Dog Breed :",mydog.breed)
print("My Dog Species :", mydog.species)

##########################################################
# ----------------------- Methods -----------------------#
# are the functions defined inside a class               #
# essential in dividing responsibility and encapsulation #
##########################################################

class Circle():

    # class obj. attribute
    pi = 3.14

    # initialize attribute radius
    def __init__(self, radius = 1):
        self.radius = radius
    
    # method to calculate area
    def area(self):
        return self.radius**2 * Circle.pi

    # setter method
    def set_radius(self, new_r):
        self.radius = new_r

mycircle = Circle(8)
print(mycircle.radius)
print(mycircle.area())

# change mycircle radius (dirty way)
mycircle.radius = 45
print(mycircle.area())

# change mycircle radius using setter (logical & cleaner)
mycircle.set_radius(65)
print(mycircle.area())

###############
# Inheritance #
###############

class Animal():

    def __init__(self):
        print ("Animal Created !")

    def whoAmI(self):
        print("Animal !")
    
    def eat(self):
        print("Animal Eating !")

# inherited class
class Cat(Animal):
    def __init__(self):
        # Animal.__init__(self)
        print("Cat Created !")

    def meow(self):
        print("Mew Mew !")

    def eat(self):
        print("Cat Eating !")

mycat = Cat()
mycat.whoAmI() # inherited
mycat.eat() # inherited + Method Overriden
mycat.meow()

###################
# Special Methods #
###################

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # string method
    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)

    # len method
    def __len__(self):
        return self.pages

    # del method
    def __del__(self):
        print("Book '{}' has been destroyed".format(self.title))

mybook = Book("Doc Hunter : A Gaming Love Story", "chankruze", 412)
print(mybook) # needs string representation to be able to print our own functions
print(len(mybook))
del mybook