package com.wordpress.geekofia;

class CheckingAccount extends com.wordpress.geekofia.BankAccount {
    int limits = 3 ;

    void checking() {
        System.out.println("======= Checking Account Info ========");
        System.out.println(" " );
        System.out.println(" Account Holder      : " + accountHolder);
        System.out.println(" Total Account limit :" + " $" + account);
        System.out.println(" Current Balance     :" + " $" + balance );

        System.out.println(" Maximum Limits      : " + limits);
        System.out.println(" " );

    }

}
