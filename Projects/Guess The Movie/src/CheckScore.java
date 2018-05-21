package com.geekofia;

/**
 * This class has a constructor that sets up and initialises fields and variables ready for the class to be used.
 * It has one method that takes in a guess. It processes the guess and then updates its private fields.
 * At the bottom of this class are its getter methods. These make the classes fields publicly (or package in this case)
 * available without allowing them to be changed.
 */
class CheckScore {

    /**
     * Initialise the classes fields
     */

    // The movie the system chose
    private String chosenMovie;

    // The correct letters guessed so far and remaining spaces
    private String correctGuesses;

    // True if the player guessed a letter correctly
    private boolean score;

    // Letters that have been incorrectly guessed
    private String incorrectGuesses;

    // The number of characters in the movie title. This number reduces by 1 each time a character is found.
    private int lettersToGuess;

    /**
     * The classes Constructor - When called it creates an instance of CheckScore.class with initialised variables
     * This constructor is called from GuessTheMovie.class like this: CheckScore myMovie = new CheckScore(chosenMovie);
     * @param chosenMovie the movie randomly chosen by the system
     */
    CheckScore(String chosenMovie) {

        // Assign the value of {@param chosenMovie} to this classes chosenMovie
        this.chosenMovie = chosenMovie;

        // Initialise the incorrectGuesses variable
        incorrectGuesses = "";

        // Initialise the lettersToGuess number
        lettersToGuess = 0;

        // Create an empty variable to hold the underscores in.
        StringBuilder movieToGuess = new StringBuilder();

        // Create the blanks and spaces by looping through each character in the movie title
        for (char blanksAndSpaces : chosenMovie.toCharArray()) {

            // If a letter or number is found add an underscore
            if (Character.isLetterOrDigit(blanksAndSpaces)) {
                movieToGuess.append("_");
                lettersToGuess++;
            }

            // If a space is found add a space
            if (Character.isWhitespace(blanksAndSpaces)) {
                movieToGuess.append(" ");
            }
        }
        // correctGuesses is now ready, so assign its new value
        correctGuesses = movieToGuess.toString();
    }

    /**
     * updateScore method finds any instances of the guess'ed character in the chosenMovie string
     * If found it places the guess'ed character at the same index within the correctGuesses string
     * This way correctGuesses is slowly filled by the characters from chosenMovie.
     * @param guess - The 'guess'ed character
     */
    void updateScore(char guess) {

        // Reset score to false
        score = false;

        // Turn correctGuesses into a character array that we can easily search and update
        char[] guessedSoFar = correctGuesses.toCharArray();

        // Now iterate through chosenMovie twice (once for upper and once for lower case characters)
        // to find the index(s) of the 'guess'ed letter if it exists.
        for (int x = 0; x < 2; x++) {

            // Whatever case we receive the guessed letter in,
            // change it to lower case for the first check
            if (Character.isUpperCase(guess) && x == 0) {
                guess = Character.toLowerCase(guess);
            }

            // For the second check, change the character to uppercase
            if (x == 1) {
                guess = Character.toUpperCase(guess);
            }

            // Loop through every character in the chosenMovie
            for (int i = 0; i < chosenMovie.length(); i++) {

                // If the guess'ed character is found within the chosenMovie,
                if (chosenMovie.charAt(i) == guess) {

                    // update score to true.
                    score = true;

                    // replace the character at that location within the correctGuesses and,
                    guessedSoFar[i] = chosenMovie.charAt(i);

                    // and reduce the amount of letters left to guess by 1
                    lettersToGuess--;
                }
            }
        }
        // If score is set to true..
        if (score) {

            // Update the value of correctGuesses
            correctGuesses = String.valueOf(guessedSoFar);

        } else {

            // If score is false, the guess'ed letter was not found, so add the guess'ed
            // letter to the incorrectGuesses list
            incorrectGuesses += Character.toLowerCase(guess) + " ";
        }
    }

    // Getter method to retrieve the chosen movie
    String getChosenMovie() {
        return chosenMovie;
    }

    // Getter method for the current state of the guesses
    String getCorrectGuesses() {
        return correctGuesses;
    }

    // If true player guessed a letter correctly
    boolean getScore() {
        return score;
    }

    // The letters not in the movie
    String getIncorrectGuesses() {
        return incorrectGuesses;
    }

    // Getter for the number of letters in the title
    int getLettersToGuess() {
        return lettersToGuess;
    }
}