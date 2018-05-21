import java.util.InputMismatchException;
import java.util.Scanner;

public class Main{
        public static void main(String[] args) {
            String[] months = {"Jan", "Feb", "Mar", "Apr", "May", "Jun",
                    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
            Scanner scanner = new Scanner(System.in);
            try {
                int month = scanner.nextInt();
                System.out.print(months[month]);
            } catch (IndexOutOfBoundsException e) {
                System.out.print("Index is out of bounds");
            } catch (InputMismatchException e) {
                System.out.print("Input mismatch");
            }

        }
}
