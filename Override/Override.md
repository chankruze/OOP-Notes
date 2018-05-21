# Override
When a class extends another class, all public methods declared in that parent class are automatically included in the child class without you doing anything.

However, you are allowed to **override** any of those methods. Overriding basically means re-declaring them in the child class and then re-defining what they should do.

Going back to our chess example, assume you're implementing the isValidMove method in the `Rock` class.

The `Rock` class extends the `Piece` class that already includes a definition of the `isValidMove` method.
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
Now let's implement a custom version of that method inside the Rock class:
```
class Rock extends Piece{
   boolean isValidMove(Position newPosition){
      if(newPosition.column == this.column || newPosition.row == this.row){
         return true;
      }
      else{
         return false;
      }
   }
}
```
Notice how both method declarations are identical, except that the implementation in the child class has different code customizing the validity check for the Rock piece. Basically it's checking that the new position of the rock has the same column value as the current position (which means it's trying to move up or down), or has the same row position which means it has moved sideways, both valid movements for a Rock piece.

Remember that `this.position.column` and `this.position.row` are the local fields of the Rock class holding the current position of that piece.

We can also do the same for all the other piece types, like for example the Bishop class would have slightly different implementation:
```
class Bishop extends Piece{
   boolean isValidMove(Position newPosition){
      if(Math.abs(newPosition.column - this.column) == Math.abs(newPosition.row - this.row)){
         return true;
      }
      else{
         return false;
      }
   }
}
```
For the `Bishop`, since it can only move diagonally, we'd want to check that the number of vertical steps is equal to the number of horizontal steps. That is, the difference between the current and new column positions is the same as the difference between the current and new row positions.

I've used `Math.abs` which takes the absolute value of that difference to always be a positive value, allowing this check to work for all 4 diagonal directions.

Perfect, now try to override this method for the Queen class, remember, a Queen can move diagonally or in straight lines.
