package com.geekofia;

import java.io.File;
import java.io.IOException;
import java.util.Scanner;

class GuessTheMovie {

    public static void main(String[] args) throws IOException {

        // Call method setUpMovie and assign the result to chosenMovie to get our movie setup and ready
        String chosenMovie = setUpMovie();

        // Instantiate a new CheckScore object with the chosen movie.
        CheckScore myMovie = new CheckScore(chosenMovie);

        // Display the movie (for testing purposes only)
        System.out.println("Random movie  is: "
                + myMovie.getChosenMovie() + " "
                + myMovie.getLettersToGuess());

        // Guesses
        int guessesOutOfTen = 0;

        // While loop for 10 guesses
        while (guessesOutOfTen < 10) {

            // Print out correct guesses and blank spaces
            System.out.println("You are guessing: "
                    + myMovie.getCorrectGuesses()
                    + " Letters left to guess: "
                    + myMovie.getLettersToGuess());

            // Print out any incorrect letters guessed so far
            System.out.println("You have guessed ("
                    + guessesOutOfTen
                    + ") wrong letters: "
                    + myMovie.getIncorrectGuesses());

            // Request the player input a guess
            System.out.println("Guess a letter: ");

            // Read the players input
            Scanner stringIn = new Scanner(System.in);

            // Read the first letter or number from the input
            char guess = stringIn.next().charAt(0);

            // If the value of 'guess', in lowercase or uppercase, is NOT present within correctGuesses and is NOT
            // present within incorrectGuesses, this is a new character, so execute the body of the loop.
            if (!myMovie.getCorrectGuesses().contains(String.valueOf(Character.toLowerCase(guess))) &&
                    !myMovie.getCorrectGuesses().contains(String.valueOf(Character.toUpperCase(guess))) &&
                    !myMovie.getIncorrectGuesses().contains(String.valueOf(Character.toLowerCase(guess))) &&
                    !myMovie.getIncorrectGuesses().contains(String.valueOf(Character.toUpperCase(guess)))) {

                // Use our instance of CheckScore called myMovie to see if this guess is in the film title
                myMovie.updateScore(guess);

                // Use myMovies getScore getter method to see if score is set to false
                if (!myMovie.getScore()) {
                    // Player didn't find a letter, so increase the value of guessesOutOfTen
                    guessesOutOfTen++;
                }

                // Else the value of 'guess' has been used before,
            } else {
                // so reject it nicely
                System.out.println("You've already used that letter! Try again...");

            }

            // If you run out of guesses, game over
            if (guessesOutOfTen == 10) {
                System.out.println("You ran out of guesses, GAME OVER!!");
            }

            // If you guess all of the letters and you still have guesses left, you win
            if (myMovie.getLettersToGuess() == 0) {
                System.out.println("You have guessed '" + myMovie.getChosenMovie() + "' correctly.");
                break;
            }
        }
    }

    /**
     * This method takes no input. It creates an empty string array, then fills it with movie titles from the
     * given text file. While it is processing the movie titles it removes any special characters making the
     * game more fair and a little easier to play.
     */
    private static String setUpMovie() {

        // String array to hold the movies. We have to assume we don't know how many movies there are. So setting
        // the default value to 100. If there is a problem with the file we will handle it in the try catch block
        String[] movies = new String[100];

        // Counter for the number of lines (movies) in the text file
        int lineNo = 0;

        try {
            // Open the movie file
            File file = new File("movies.txt");

            // Setup a scanner to read the contents of the file
            Scanner fileScanner = new Scanner(file);

            // Loop through each line in the text file and..
            while (fileScanner.hasNextLine()) {
                // fill up the movies string array, whilst removing any special characters
                // as this makes the game more fair
                movies[lineNo] = fileScanner.nextLine().replaceAll("[^a-zA-Z0-9 ]", "");
                // increment the line No each time we add a new movie
                lineNo++;
            }

        } catch (Exception e) {

            // If any error occurs
            e.printStackTrace();
            // Display a message to help point the user in the right direction
            System.out.println("Game is configured for up to 100 movies "
                    + "only. Does your file 'movies.txt' contain more?");
        }

        // Generate a random number based on the number of movies (lines) found
        int randomLineNo = (int) (Math.random() * lineNo);

        // Use the random number on the index of the movies array to return the associated movie.
        // Trim off any spaces.
        return movies[randomLineNo].trim();
    }
}