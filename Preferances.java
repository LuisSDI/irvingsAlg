/**
 * Jack Merryman 5/1/2018
 * Xavier University 
 * Computer Science Capstone Project
 * Comparison Class 
 * */



import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.*;
import javafx.util.Pair;

public class Preferances
{
    static ArrayList<Pair<Integer,Integer>> allPlayers = new ArrayList<Pair<Integer,Integer>>();
    static ArrayList<Pair<Integer,Integer>> skillTree = new ArrayList<Pair<Integer,Integer>>();
    static ArrayList<Integer> PlayersofSkills = new ArrayList<Integer>();
    public static void main(String args[]) throws FileNotFoundException
    {
        Scanner(args[0]);   // Calls Scanner on given file name
        rank();         // Calls rank on a given player
    }
    /** 
     *  
     *  Comparison class for finding the difference in skill rating between 2 given players
     *    
     *  */
    public static int compat(Integer x, Integer y)
    {
    	//Takes two given players and returns the difference between them as the skill difference. 
        int pAs = x;
        int pBs = y;
        int skillDifference = pAs - pBs;
        return skillDifference;
    }
    /** 
     *  
     *  Looks through a given File, splits the second "," adding all Skill ratings to an array in order by the player. 
     *  
     *  */
    public static void Scanner(String args) throws FileNotFoundException {
        Scanner reader = new Scanner(new File(args));
        while(reader.hasNext())
        {
            String i = reader.nextLine();
            String[] test = i.split(",");
            Pair<Integer,Integer> p1 = new Pair<>(Integer.parseInt(test[0]),Integer.parseInt(test[2]));
            allPlayers.add(p1);
        }
        reader.close();
    }
    /** 
     *  
     *  Takes a given player and their skill, then runs the compat
     *  method on it and every other playe's skill rating. Then adds
     *  the Player and skill difference to a HashMap for that given player  
     * @throws FileNotFoundException 
     *  
     *  */    
    public static void rank() throws FileNotFoundException
    {
        int thePlayer = 0;
        PrintWriter printWriter1 = new PrintWriter(new File("Players Skill Prefs.txt"));
        printWriter1.print(0+" ");
    	int z = 0;
    	while(z < allPlayers.size()) 
    	{
    		printWriter1.print(0);
    		z++;
            if(thePlayer != allPlayers.size())
            {
                printWriter1.print(" ");
            }
    	}
    	printWriter1.print(0);
    	printWriter1.println();
        while(thePlayer < allPlayers.size())
        {	
        	int i =0;
        	// We specify a player here called "thePlayer" this value is that 
        	// carries us through the rest of the loops in the called methods 
        	players(thePlayer);
        	skills(thePlayer);
        	// These prints included the exact JSON format that the SRP needs to run 
        	printWriter1.print(0+" ");
        	while(i < PlayersofSkills.size()) {
        		printWriter1.print(PlayersofSkills.get(i));
        		i++;
                if(thePlayer != allPlayers.size())
                {
                    printWriter1.print(" ");
                }
           }
            printWriter1.print(0);
            thePlayer++;
        	PlayersofSkills.clear();   
        	if(thePlayer != allPlayers.size())
    		{
        		printWriter1.println();
        	}
        }
        printWriter1.close();
    }
    
    /** 
     * 
     * Players is the method that calls the Compare method on the given players. 
     * Looping through all players against a specified player and adding the
     * players ID and Skill Difference to a list of pairs for specified player
     * 
     * */
    public static void players(int thePlayer)
    {
        int i = 0;
        int y = 0;
        while(i < allPlayers.size())
        {
            int skillcomp = compat(allPlayers.get(thePlayer).getValue(), allPlayers.get(y).getValue());
            // We use the absolute value here because we want the closest number to 0 to be first in the list
            // rather than a negative number because the smallest in the eyes of sorting. 
            Pair<Integer,Integer> p1 = new Pair<>(allPlayers.get(y).getKey(),Math.abs(skillcomp));
            skillTree.add(p1);
            i++;
            y++;
        }
    }
    
    /**
     * 
     * The Skills method calls the sorting method on so that it can 
     * make an ordered list of players based on their skills for the specified player. 
     * 
     * */
    public static void skills(int thePlayer)
    {
       int j = 0;
       sorting();
       while(j < skillTree.size())
            {
            	if(skillTree.get(j).getKey() == thePlayer+1)
            	{ j++; 
            	} else {
            		PlayersofSkills.add(skillTree.get(j).getKey());
                j++;
                }
            }
        skillTree.clear();
    }
    
    /**
     * 
     * The sorting method uses comparator to sort the list of players based on their skills 
     * in the pairs so that we has an ascending list of people.
     * 
     * */
    public static void sorting()
    {
        skillTree.sort(new Comparator<Pair<Integer, Integer>>() {
            @Override
            public int compare(Pair<Integer, Integer> o1, Pair<Integer, Integer> o2) {
                if (o1.getValue() > o2.getValue()) {
                    return 1;
                } else if (o1.getValue().equals(o2.getValue())) {
                    return 0; // You can change this to make it then look at the
                              //words alphabetical order
                } else {
                    return -1;
                }
            }
        });
     }
}