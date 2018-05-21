# The Comparable Interface

A very popular interface in Java is the [Comparable Interface](https://docs.oracle.com/javase/8/docs/api/java/lang/Comparable.html).

This interface includes a single method definition called `compareTo` which takes an object as an input parameter of the same type and compares both objects ("this" object against the input argument object).

The main purpose of this interface is to give any class a chance to describe how to compare 2 objects of that class against each other. This will be really handy when we get to sorting or searching for such objects of that type.

For example:

Assume you have a class that represents a book:
```
public class Book{
   int numberOfPages;
   String title;
   String author;
}
```
And you are asked to implement the Comparable Interface so that you can sort the books according to the following criteria:

   1. If a book has more pages than the other, then the book with the more pages goes first.
   2. If both books have the same number of pages, then sort by the title alphabetically.
   3. If both books have the same number of pages and the same title, then sort by the author alphabetically.

Before we start coding, let’s go through how the compareTo method should work:

The compareTo method takes a single input parameter (let's refer to it as the "specified object") and since this method belongs to an object itself (let's refer to it as "this object"), then the method simply compares the "specified" object against "this" object.

According to the documentation, there are 3 possible outcomes when comparing any 2 objects:

   1. "This" object is considered less than the "specified" object
   2. "This" object is considered equal to the "specified" object
   3. "This" object is considered greater than the "specified" object

Respectively, for each of those cases, `compareTo` method should return:

   1. A negative integer (any number less than 0)
   2. zero (0)
   3. A positive integer (any number greater than 0)

Ok, now that we've got everything well defined, let's start coding:
```
public class Book implements Comparable<Book>{
   public int compareTo(Book specifiedBook) {
      // First check if they have different page counts
      if(this.numberOfPages != specifiedBook.numberOfPages){
         // this will return a negative value if this < specified but will return a positive value if this > specified
         return this.numberOfPages - specifiedBook.numberOfPages;
      }
      // If page counts are identical then check if the titles are different
      if(!this.title.equals(specifiedBook.title){
         return this.title.compareTo(specifiedBook.title);
      }
      // If page titles are also identical then return the comparison of the authors
      return this.author.compareTo(specifiedBook.author);
    }
}
```
