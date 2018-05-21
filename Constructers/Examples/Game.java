/**
 * Written and tested by ギョクフィア on sat,05 th May 2018
 */
public class Game {
    int score;
    //Default constructor
    Game(){
        score=0;
        System.out.println(score);
    }
    //Constructor by starting score value
/**
 * @parm startingScore
 * @return constructors don't have return type
 */
    Game(int startingScore){
        score=startingScore;
        System.out.println(score);
    }

}
