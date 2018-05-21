class Rock extends Piece{
    boolean isValidMove(Position newPosition) {
        // First call the parent's method to check for the board bounds
        // If we passed the first test then check for the specific rock movement
        return super.isValidMove(newPosition) && (newPosition.column == this.column || newPosition.row == this.row);

    }
}