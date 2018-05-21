# The Chess Example

We've seen how Inheritance allows you to extend classes and add more functionality to them.

Sometimes you not only want to extend the functionality of a class, but also modify it slightly in the child class.

For example, say you're building a Java chess game.

![Chess Board](http://chesssetup.com/wp-content/uploads/2016/02/Chess-Board-Set-Up-480x480.png)

A good Java design will have a **class** for each piece type:

![Piece Type](https://image.ibb.co/fTkLRJ/Screenshot_46.png)

And they should all inherit from a common base class: `Piece`

**Why?**

Because according to the concept of polymorphism, you could represent the chess-board as a 2D array of `Piece` objects, and then each cell in the 2D array can contain any of the child classes that extend the `Piece` class.

### Other classes
To store this 2D array we will need a class that represents the Game itself:
```
class Game{
   Piece [][] board;
   // Constructor creates an empty board
   Game(){
      board = new Piece[8][8];
   }
}
```
And finally, a simple class called `Position` that has nothing more than a row value and a column value to represent a specific slot on the board.
```
class Position{
   int row;
   int column;
   // Constructor using row and column values
   Position(int r, int c){
      this.row = r;
      this.column = c;
   }
}
```
That way, the `Piece` class can include a field variable of type `Position` that stores the current position of that piece on the board:
```
class Piece{
   Position position;
}
```
Now, since all piece types inherit from the same parent class `Piece`, they will all share any methods declared in that class.

For example:

It will be useful to have a method that checks if a potential movement of a piece is a valid one. Even though each piece type has a unique movement capability, any piece (regardless of its type) has to - at the very least - stay within the bounds of the chess board.

So, a good idea would be to include a method called `isValidMove` inside the `Piece` class that takes a potential new position and decides if that position is within the bounds of the chess board.

```
class Piece{
   boolean isValidMove(Position newPosition){
      if(newPosition.row>0 && newPosition.column>0 
         && newPosition.row<8 && newPosition.column<8){
         return true;
      }
      else{
         return false;
      }
   }
}
```

Since each of the child classes inherits from that `Piece` class, each will automatically include this method, which means you can call it from any of those classes directly.

For example:
```
Queen queen = new Queen();
Position testPosition = new Position(3,10);
if(queen.isValidMove(testPosition)){
   System.out.println("Yes, I can move there.");
}
else{
   System.out.println("Nope, can't do!");
}
```
**Q**: What will the above code print ?

**Ans** : Nope, can't do!

What we've done so far can be considered as a good start for checking the validity of the movement of a piece on the board. However, each piece type has a different pattern of allowed movements, which means that each of those child classes needs to implement the `isValidMove` method differently!

Luckily, Java not only offers a way to inherit a method from a parent class but also modify it to build your own custom version of it.







