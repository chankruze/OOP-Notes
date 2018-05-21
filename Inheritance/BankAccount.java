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