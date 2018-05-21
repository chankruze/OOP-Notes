# Constructors

Constructors are special types of methods that are responsible for creating and initializing an object of that class.
## Creating a constructor

Creating a constructor is very much like creating a method, except that:

   - Constructors don't have any return types
   - Constructors have the same name as the class itself

They can however take input parameters like a normal method, and you are allowed to create multiple constructors with different input parameters.

Here's an example of a simple constructor for a class called `Game`
```
class Game{
   ...
   // Constructor
   Game(){
      // Initialization code goes here
   }
   ...
}
```
## Default constructor

A Default constructor is one that doesn't take any input parameters at all!

It's optional, which means if you don't create a default constructor, Java will automatically assume there's one by default that doesn't really do anything.

However, if the class has fields that need to be initialized before the object can be used, then you should create one that does so.

For example, assume we have a class `Game` that has an integer member field score, we'd like to make sure that any object of type `Game` will start with the `score` value set to `0`. To do so, we need to create a default constructor that will initialize the `mScore` field
```
class Game{
   int mScore;
   // Default constructor
   Game(){
      // Initialize the score here
      mScore = 0;
   }
}
```
## Parameterized constructor

As we've mentioned earlier, a constructor can also take input parameters.

Let's assume that some games start with a positive score value and not just 0, that means we need another constructor that takes an integer parameter as an input, and uses that to initialize the score variable.
```
class Game{
   int score;
   // Default constructor
   Game(){
      score = 0;
   }
   // Constructor by starting score value
   Game(int startingScore){
      score = startingScore;
   }
}
```
## Accessing a constructor

Unlike normal methods, constructors cannot be called using the dot `.` modifier, instead, every time you create an object variable of a class type the appropriate constructor is called. Let's see how:
### The `new` keyword

To create an object of a certain class, you will need to use the `new` keyword followed by the constructor you want to use, for example:

`Game tetris = new Game();`

This will create an object called tetris using the default constructor (i.e. tetris will have an initial score value of 0)

To create a game that is initialized with a different starting score you can use the second constructor:

`Game darts = new Game(501);`

### The `null` keyword

If you do not initialize an object using the `new` keyword then its value will be set to something called `null`. `null` simply refers to an empty (uninitialized) object. `null` objects have no fields or methods, and if you try to access a `null` object's field or call its method you will get a runtime error.

In some cases, you might want to explicitly set an object to `null` to indicate that such object is invalid or yet to be set. You can do so using the assignment operation:

`Game darts = null;`

### The `this` keyword

[Details on this keyword](https://www.javatpoint.com/this-keyword)

## Why multiple constructors?

You might be wondering why do we still need to keep the default constructor now that we have another constructor that can create a game object with any starting score value (including `0`)?

Good point, however, it's considered a good practice to always include a default constructor that initializes all the fields with values that correspond to typical scenarios. Then you can add extra parameterized constructors that allow for more customization when dealing with less common cases.
### But you said the default constructor is optional!

As we've mentioned earlier, you have the option to not create any constructors at all! The class will still be valid and you will be able to create objects using the same syntax of a default constructor. Exactly as if you had created an empty default constructor.

However, this privilege goes away once you create any constructor of your own! Which means if you create a parameterized constructor and want to also have a default constructor, you will have to create that default constructor yourself as well.
