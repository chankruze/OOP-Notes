# The `main` method

A Java program can be as small as a single class, but usually a single program will be made up of tens or even hundreds of classes!

A good Java program is one that divides the logic appropriately so that each class ends up containing everything related to that class, and nothing more!

Classes would be calling each other's methods and updating their fields to make up the logic of the entire program all together!

BUT, where should the program start from exactly? In other words, if a method can call another method and that method can call another, which method will start this sequence the very first time?

The answer is the main method! It looks like this:

```
public static void main(String [] args){
   // Start my program here
}
```

Let's break it down:

   - `public`: Means we can run this method from anywhere in our Java program
   - `static`: Means it doesn't need an object to run, which is why the computer starts with this method before even creating any objects
   - `void`: Means the main method doesn't return anything, it just runs when the program starts, and once it's done the program terminates
   - `main`: Is the name of the method
   - `String [] args` : Is the input parameter (array of strings)

This main method is the starting point for any Java program, when a computer runs a Java program, it looks for that main method and runs it.

Inside it you can create objects and call methods to run other parts of your code. And then when the main method ends the program terminates.

If this main method doesn't exist, or if there's more than one, the Java program won't be able to run at all!

The main method can belong to any class, or you can create a specific class just for that main method which is what most people do.

