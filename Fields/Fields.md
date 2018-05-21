# Fields

The fields of an object are all the data variables that make up that object. They are also sometimes referred to as `attributes` or `member variables`.

These fields are usually made up of `primitive types`like integers or characters, but they can also be `objects` themselves.

For example a `book` object may contain fields like `title`, `author` and `numberOfPages`.

Then a `library`object may contain a field named `books` that will store all book objects in an array.

## Accessing fields:

Accessing a field in an object is done using the dot modifier `.`

For example, if we had an object called `book`that contains these fields:
```
String title;
String author;
int numberOfPages;
```

To access the title field you would use

`book.title`

This expression is just like any other string, which means we can either store it in a string variable:

`String myBookTitle = book.title;`

Or use it directly as a string itself and perform operations like printing it:

`System.out.println(book.title);`

## Setting Fields

We can also change a field’s value. Say you want to set the number of pages in a book to 234 pages:

`book.numOfPages = 234;`

