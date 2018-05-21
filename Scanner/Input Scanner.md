# Input Scanner

The most flexible and common way to read an input from a user is by asking them to type in something and wait till they respond.

Just like we've seen how this command will print "Hello World" to the command line as an output:
```
System.out.println("Hello World!");
```
You can also ask the user to type in a message and then your Java program can read it into a variable and use it.

This is done using a Java class called `Scanner`.

First, to be able to access this class, you have to point your program to the `java.util` library that includes the `Scanner` class. You do that by typing this at the very top of the file
```
import java.util.Scanner;
```
We will talk more about including packages and libraries later.

A Scanner allows the program to read any data type from a particular input, if we create the scanner object like this:
```
Scanner scanner = new Scanner(System.in);
```
Then the scanner will be reading from the System's input (hence `System.in`) which is basically the command line.

It will continue to read whatever the user is typing until they hit "enter" then the program continues to execute.

Once the scanner object has been created, you can use it to read a `String`, an `integer` or an `entire line`.

Calling the method `nextLine()` in that scanner object will return a String that contains everything the user has typed in before they hit "enter".
```
scanner.nextLine();
```
For example:
```
System.out.println("Enter your address: ");
Scanner scanner = new Scanner(System.in);
String address = scanner.nextLine();
System.out.println("You live at: " + address);
```
The above code will wait until the user types in their address, then stores it into the variable `address` and then prints it back to the user.

If we want to read a number into an integer variable instead of the entire line we should use the`nextInt()`method:
```
System.out.println("Enter your grade: ");
Scanner scanner = new Scanner(System.in);
int grade = scanner.nextInt();
if(grade > 90){
   System.out.println("Wow! you did well!");
}else{
   System.out.println("Not bad, but you can do better next time!");
}
```

