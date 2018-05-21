package com.wordpress.geekofia;

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
