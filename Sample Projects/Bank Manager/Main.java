package  com.wordpress.geekofia;

public class Main {

    public static void main (String [] args){

        com.wordpress.geekofia.BankAccount myAccount = new com.wordpress.geekofia.BankAccount();
        com.wordpress.geekofia.CheckingAccount check = new com.wordpress.geekofia.CheckingAccount();
        com.wordpress.geekofia.SavingsAccount saving = new com.wordpress.geekofia.SavingsAccount();
        com.wordpress.geekofia.CertificateOfDeposit COD = new com.wordpress.geekofia.CertificateOfDeposit();

        myAccount.showMainAccountinfo();
        saving.savings();
        check.checking();
        COD.certificate();

    }
}
