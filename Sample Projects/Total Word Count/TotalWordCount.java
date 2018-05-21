/*
 * Total Word Count
 * Created by GEEKOFIA sun,May 6 2018
 */
import java.io.File;
import java.util.Scanner;

public class TotalWordCount {
    // Exception must declared to be thrown
    public static void main (String [] args) throws Exception{
        File file = new File("deathmademistake.txt");
        Scanner scanner = new Scanner(file);

        int totalWords = 0;
        while (scanner.hasNextLine()){
            String line = scanner.nextLine();
            // Counts words per line by spliting every line and add those to totalWords variable.
            totalWords += line.split("").length;
        }
        System.out.println("Death Make Mistake File Has : " + totalWords + " words.");
    }
}