/**
 * Jack Merryman 5/1/2018
 * Xavier University 
 * Computer Science Capstone Project
 * DeckDataGen Class 
 * */
import java.util.Random;
import java.io.PrintWriter;
import java.io.File;
import java.io.FileNotFoundException;

public class DeckDataGen
{
	public static void main(String args[])
    {
    	try {
			genData(args[0], args[1], args[2], args[3]);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
    }
	/**
	 * 	The genData takes in 3 args, amount of players, amount of decks and skill cap of a player.
	 * then randomly generating values for the decks and skills. 
	 * finally making a file of the specified tournament
	 * */
	public static void genData(String file, String args1, String args2, String args3) throws FileNotFoundException
	{ 
	    PrintWriter printWriter1 = new PrintWriter(new File(file));
		Random rand = new Random();
		int i = 0;
			while(i < Integer.parseInt(args1))
			{
				i++;
				int d = rand.nextInt(Integer.parseInt(args2)) + 1;
				int s = rand.nextInt(Integer.parseInt(args3)) + 1;
				String skill = Integer.toString(s);
				String deck = Integer.toString(d);
				String player = Integer.toString(i);
				printWriter1.println(player + "," + deck + "," + skill);
			}
			printWriter1.close();	
		}
}
