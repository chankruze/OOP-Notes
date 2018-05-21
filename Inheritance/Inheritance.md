# Inheritance
Inheritance in java is used to imoprt fiels from the parent class and accessing them without rewriting.
It is done using `extends` keyword.

For ex:
```
package com.wordpress.geekofia;

public class BankAccount {
    String accountHolder = "GEEKOFIA";
    String accountNumber = "000000223344";
    int account = 1000000;
    double balance = 93564;

    void showMainAccountinfo() {
        System.out.println("========= Main Account Info ==========");
        System.out.println(" " );
        System.out.println(" Account Holder      : " + accountHolder);
        System.out.println(" Account Number      : " + accountNumber);
        System.out.println(" Total Account limit :" + " $" + account);
        System.out.println(" Current Balance     :" + " $" + balance );
        System.out.println(" " );



    }

}
```
We can import common fields like `accountHolder` , `accountNumber`,`balance` from parent class  `BankAccount` to children classes `savingsAccount` and can access the fileds without rewriting them.
```
class SavingsAccount extends com.wordpress.geekofia.BankAccount {
    int transfers = 5;

    void savings() {
        System.out.println("======= Savings Account Info =========");
        System.out.println(" " );
        System.out.println(" Account Holder      : " + accountHolder);
        System.out.println(" Total Account limit :" + " $" + account);
        System.out.println(" Current Balance     :" + " $" + balance );

        System.out.println(" Maximum Transfers   : " + transfers);
        System.out.println(" " );

    }
}
```
For more example explore Bank Manager folder in Sample Projects.