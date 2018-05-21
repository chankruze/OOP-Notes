# super

SUPER! "`super`" is actually another Java keyword that we will be using next!

It is important to note that once you override a method, you basically ignore everything that was in the parent class and instead have your own custom implementation in the child class (literally overwriting it)!

In our case, we don't want to throw away the parent implementation. We actually want to continue to use the original method, and ADD the extra checks for each child class individually.

This is where we get to use the "`super`" keyword!

You are allowed to re-use the parent method in the child class by using the "`super`" keyword, followed by a dot and then the method name:
```
super.isValidMove(position);
```
Using the keyword super here means that we want to run the actual method in the super (or parent) class from inside the implementation in "this" class.

Which means in each of the child classes, before you get to check the custom movement, you can check if `super.isValidMove(position)` has returned false. If so, then no need to do any more checks and immediately return false; otherwise, continue checking.

The new implementation for the Rock class will look like this:
```
class Rock extends Piece{
   boolean isValidMove(Position newPosition){
      // First call the parent's method to check for the board bounds
      if(!super.isValidMove(position)){
         return false;
      }
      // If we passed the first test then check for the specific rock movement
      if(newPosition.column == this.column && newPosition.row == this.row){
         return true;
      }
      else{
         return false;
      }
   }
}
```
You can also use `super()` to call the parent's constructor. This is usually done when implementing the child's constructor. Typically you would want to first run everything in the parent's constructor then add more code in the child's constructor:
```
class Rock extends Piece{
   // default constructor
   public Rock(){
      super(); // this will call the parent's constructor
      this.name = "rock";
   }
}
```
**Note**: If a child's constructor does not explicitly call the parent's constructor using super, the Java compiler automatically inserts a call to the default constructor of the parent class. If the parent class does not have a default constructor, you will get a compile-time error.
