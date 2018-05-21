
//Example of Polymorphism

public class Person {
    String name = "Johnny Sins";
    String email = "johnnysins@brazzers.com";

    public  static  void main (String [] args) {
        /*
         * Calling Teacher & Pornstar constructure using Person type
         * without calling as : Teacher call1 = new Teacher();
         */
        Person call1 = new Pornstar();
        Person call2 = new Teacher();

    }

}
