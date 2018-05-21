# Self Reference

Sometimes you'll need to refer to an object within one of its methods or constructors, to do so you can use the keyword `this`.

**this** is a reference to the current object — the object whose method or constructor is being called. You can refer to any field of the current object from within a method or a constructor by using `this`.
## Using `this` with a Field

The most common reason for using the `this` keyword is because a field has the same name as a parameter in the method or constructor

For example, if a Position class was written like this
```
class Position {
   int row = 0;
   int column = 0;

    //constructor
   Position(int r, int c) {
      row = r;
      column = c;
   }
}
```
A more readable way would be to use the same names (`row` & `column`) for the constructor parameters which means you will have to use the `this` keyword to seperate between the fields and the paramters:
```
class Position {
   int row = 0;
   int column = 0;

    //constructor
   Position(int row, int column) {
      this.row = row;
      this.column = column;
   }
}
```
In the second snippet, the constructor `Position` accepts the parameters `row` and `column`, but the class Position also includes two fields with the exact same name.

Using `this.row` compared to `row` means that we are referring to the **field** named `row` rather than the input parameter.

There are plenty more uses for the keyword `this` that you can check out [here](https://docs.oracle.com/javase/tutorial/java/javaOO/thiskey.html).
