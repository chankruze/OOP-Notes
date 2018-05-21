## Interesting fact

Given 10 chances to guess a number between 1 and 100 (with "smaller than" or "greater than" feedback), is more than enough for you to ALWAYS win!

The trick is to use something called the [Binary Search Algorithm](https://en.wikipedia.org/wiki/Binary_search_algorithm)

It's a very clever search technique where you cut your search range by half every time you make a new guess:

   - You start with the range [1 - 100]
   - Always start your first guess as 50 (midpoint between 1 and 100)
   - If the random number was smaller, then it must be between [1 - 50]
   - If the random number was greater, then it must be between [50 - 100]

   - Repeat the same technique by guessing the midpoint of the new range:
      - If the new range is [1 - 50] then guess 25
      - If the new range is [50 - 100] then guess 75

   - And so on, until you get it right.

In fact, you will only need **7** guesses at most (for the range 1-100).

Binary Search is a very popular algorithm used by computer scientists all the time.

Go ahead and try this strategy while playing this game ;)
