# Methods (public vs private)

With methods, it's common to have a mix of private and public methods.

The private methods are usually known as **helper methods**, since they can only be seen and called by the same class, they are usually there to organize your code and keep it simple and more readable.

The public methods are the actual actions that the class can perform and are pretty much what the rest of the program can see and call.

Here's an example of when you'd want to use public methods vs private methods

```
class Person{
   private String userName;
   private String SSN;
   private String getId(){
      return SSN + "-" + userName;
   }
   public String getUserName(){
      return userName;
   }
   public boolean isSamePerson(Person p){
      if(p.getId().equals(this.getId()){
         return true;
      }
      else{
         return false;
      } 
   }
}
```
The class Person has both its fields set to **private** because if they were public then any other class will be able to change such sensitive information. Setting them to private means that only methods and constructors inside this class can do so!

The method `getId()` was also set to private so that no other class can know the social security number of any person.

However, we were still able to use that method internally when comparing this person with another person object in the `isSamePerson(Person p)` method.

This means that any other class can only call `getUserName` or `isSamePerson` and will seem as if these are the only 2 methods provided by the class Person
## Public classes

Even classes can be labeled as **public** or **private**! And even though you are allowed to label a class as **private**, it requires you to know about [nested classes](https://docs.oracle.com/javase/tutorial/java/javaOO/nested.html) which is not covered here.

So for now, make sure you label all your classes public.
What if I don't use any label at all?

We've been doing that so far anyway! What does that mean?

It's not recommended to do so, but if you do, it will default to something called "package public" which means it's as if you've labeled them public but only to the classes that are in the same package/folder. We will learn more about packages later. But again, it's always a good idea to label everything explicitly.
## But but but
... wait a second! Since I have access to all the code, can't I just go back and change all the private methods and fields and make everything public and control the universe!

Yes, but remember that this is for your own good. You're trying to design your code in a way that will prevent you from doing things you don't want to happen! You're also most likely going to be working with a team of other developers, and setting the correct access modifiers helps communicate with everyone the intended use of each part of your project.
## Summary

To summarize, it's recommended to:

   - Set all your classes to **public**
   - Set all your fields to **private**
   - Set any of your methods to **public** that are considered actions
   - Set any of your methods to **private** that are considered helper methods

