public class Main {
    public static void main(String[] args) {
        Bishop bishop = new Bishop();
        Position testPosition = new Position(3, 4);

        if (bishop.isValidMove(testPosition)) {
            System.out.println("Yes, I can move there.");
        } else {
            System.out.println("Nope, can't do!");
        }
    }
}
