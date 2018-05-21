# Methods

We might have also noticed that running actions in objects look very much like calling a function. That’s because that’s exactly what it is.

Methods in Java are functions that belong to a particular object. We will be creating methods the same way we used to created functions.

## Calling a method

To use a method we call it (just like calling a function). This is also done using the dot modifier <code>.</code>

Methods, just like any function can also take in arguments. 

For Example: Assume that our <code>book</code> object has a method called <code>setBookmark</code> that takes the page number as a parameter:

<code>void setBookmark(int pageNum);</code>

If we wanted to set a bookmark at page 12, we can call the method and pass in the page number as an argument:

<code>book.setBookmark(12);</code>

## Summary

Fields and Methods together are what make an object useful, fields store the object's data while methods perform actions to use or modify those data.

However some objects might have no fields and are just made up of a bunch of methods that perform various actions.

Other objects might only have fields that act as a way to organize storing data but not include any methods!
