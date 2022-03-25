import java.util.*;

class pizzabot {

    /*
    My plan is for the 'bot' to receive the commands to reach the houses and deliver
    the pizza by looking to see how far each axis is off the target house and iterating through
    an if-for loop to make axis x or y the same as the target and add the command to our end string;

    so if our bot is at 1,3 and our target is 5,5 our if-loop will see our x is 4 away and iterate 4 times
    through and add 1 to our x each loop and add the command E to our string; the same process will happen
    in a similar if-for loop but for our y axis until we meet our target with an end string of "EEEENND"
    */

    public static void main(String args[]) {
        
        String streetSize = args[0]; 
        String houses [] = new String[args.length - 1]; // Holds the contents of args[i] so we can extract the coordinates

        // Holds the current coordinates for our bot
        int botLocation_x = 0;
        int botLocation_y = 0;

        List<String> endString = new ArrayList<>(); // Creates String list that our commands will be inserted into

        // Loop to add our houses to our array
        for (int i = 1; i < args.length; i++){
            houses[i-1] = args[i];
        }

        for (int i = 0; i < houses.length; i++){
            System.out.println("Position " + i + " of array is: " + houses[i]);
        }
        

    }
}
