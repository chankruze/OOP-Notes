public class Main {

	public static void main(String[] args) {

		// we can store the sum in an int
		
		int sum = 0;

		// checking each number if it is divisible by 3 or 5.
		
		for (int i = 3; i < 1000; i++) {
			if (i % 3 == 0 || i % 5 == 0) {
				sum += i;
			}
		}

		System.out.println("sum of all no. = " + sum);
	}

}