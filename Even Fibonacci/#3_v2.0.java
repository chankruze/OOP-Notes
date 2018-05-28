public class Main {

	public static void main(String[] args) {

		int sum = 0, a = 1, b = 2;

		while (a <= 4000000) {
			if (a % 2 == 0)
				sum += a;

			// just to avoid creating a new variable
			b = b + a;
			a = b - a;
		}

		System.out.println(sum);
	}
}