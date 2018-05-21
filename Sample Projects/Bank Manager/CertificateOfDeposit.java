package com.wordpress.geekofia;

public class CertificateOfDeposit extends com.wordpress.geekofia.BankAccount {

    void certificate (){
        System.out.println("====== Certificate Of Deposite  ======");
        System.out.println(" " );
        System.out.println(" Account Holder      : " + accountHolder);
        System.out.println(" Total Account limit :" + " $" + account);
        System.out.println(" Current Balance     :" + " $" + balance );
        String expiry = "12/12/2020";

         System.out.println(" COD Expires on      : " + expiry);
         System.out.println("======================================");
    }
}
