/*
 * Guessing game version 1
 * Created by GEEKOFIA sun,May 6 2018
 */

import java.util.Scanner;
public class GuessingGame {
    public static void main (String [] args){
        int randomNumber = (int)(Math.random()*100)+1;
        boolean hasWon = false;
        System.out.println("I have chosen a random number between 1 and 100. ");
        System.out.println("Try to gess it ! ");
        System.out.println("You have only 10 chances ");

        Scanner scanner= new Scanner(System.in);
        for(int i=10; i>0 ; i--){
            System.out.println("You have "+ i + " guess(es) left. Choose again :(");
            int guess = scanner.nextInt();

            if(randomNumber < guess){
                System.out.println("It is smaller than " + guess + ".");
            }
            if(randomNumber > guess){
                System.out.println("It is bigger than " + guess + ".");
            }
            if(randomNumber == guess){
                hasWon = true;
                break;
            }

        }
    if(hasWon){
        System.out.println("It is correct............You Win ! ");
    }else{
        System.out.println("Game over.....You Lost ! ");
        System.out.println("The number was : " + randomNumber);
    }

    }
}
