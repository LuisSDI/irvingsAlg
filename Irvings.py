# Irving's Stable Roommate Algorithm 
# Translated and Modified by Jack Merryman
# Version 



import random
import json

# These are used to Turn on or off the debugging print statments for various methods
debugg1 = False # Phase One
debugg2 = False # Find
debugg3 = False # Seek
debugg4 = False # Phase Two
debugg5 = False # Odd Number 
debugg6 = False # Generation
debugg7 = False # Load File
debugg8 = False # RoommatesFalse


# Variables and Lists Used in the program
soln_possible = False

firstInCycle = 1
lastInCycle = 1
firstUnmatched = 1
lastInCycle = 1
nextChoice = 1
rank = 1
tail = []                       # Similar to Cycle in that it holds values used in Seek()
second = []                     # This will Hold the persons second choice while determining better/worse matches
cycle = []                      # This is used to keep track of where we are in the cycle for Seek()
leftmost = []                   # Holds the list of everyones First choice in Preferences, chanes as choices are reduced in Phase 1 & 2 
rightmost = []                  # Holds the list of everyones last choice in Preferences, chanes as choices are reduced in Phase 1 & 2 
ranking = []                    # This repersnets a Matrix (X,Y) Y's Ranking in X's Preferences
partner = []                    # This is the Ending Pairs of people that have been matched
n = 0                           # This repersents the Number of people that are being grouped by the Program
preference = []                 # Preference is a Matrix of Player IDs based on how they are ranked for a given person. 

#
# Phase One, makes the inital proposals between everyone and their first choice.
# At the end of Phase One we have completed all of proposals and updated Rightmost 
# to the reduced Last choice. 
#

def phaseOne():
        if debugg1:
                print "====================Phase One================="
        global leftmost
        global rightmost
        global ranking
        global n
        global nextChoice
        set_proposed_to = []
        for person in range(1,n+1):
                proposer = person
                while True:
                        nextChoice = preference[proposer][leftmost[proposer]]
                        current = preference[nextChoice][rightmost[nextChoice]]
                        if debugg1:
                                print "next choice",nextChoice
                                print "proposer",proposer
                                print "current",current
                                print "Rank NC P",ranking[nextChoice][proposer],"vs","Rank NC C",ranking[nextChoice][current]
                                print
                        while ranking[nextChoice][proposer] >= ranking[nextChoice][current]:
                                leftmost[proposer] = leftmost[proposer]+1
                                if debugg1:
                                        print leftmost
                                nextChoice = preference[proposer][leftmost[proposer]]
                                current = preference[nextChoice][rightmost[nextChoice]]
                        rightmost[nextChoice] = ranking[nextChoice][proposer]
                        proposer = current
                        if nextChoice not in set_proposed_to:
                                break
                set_proposed_to.append(nextChoice)
        global soln_possible
        soln_possible = proposer == nextChoice
        if debugg1:
                print "=================================================="
 
#               
# Find moved though Left and Rightmost to find the First unmatched 
# person when proposing to a new person. 
#

def find():
        if debugg2:
                print "=================Find================="
        global leftmost
        global rightmost
        global firstUnmatched
        while (leftmost[firstUnmatched] == rightmost[firstUnmatched]):
                firstUnmatched = firstUnmatched + 1
                if debugg2:
                        print "firstUnmatched",firstUnmatched
        if debugg2:
                print "======================================"

#
# Seek searches out the next choice after a change has been made to the pairings has been made
# Seek fixes the duplicate matchups that appear after Phase one
#

def seek():
        if debugg3:
                print"================Seek==================="
        global firstInCycle
        global firstUnmatched
        global tail
        global lastInCycle
        global second
        global cycle
        global rightmost
        global ranking
        global n
        if debugg3:
                print "FIC",firstInCycle
                print
        if(firstInCycle > 1):
                if debugg3:
                        print "firstInCycle",firstInCycle
                person = cycle[firstInCycle-1]
                posnInCycle = firstInCycle-1
                cycleSet = tail
        else:
                cycleSet = []
                posnInCycle = 1
                person = firstUnmatched
                if debugg3:
                        print "person fUn",person
                        print
        # This while loop cycles through the rightmost of 
        while True:
                cycleSet.append(person)
                if debugg3:
                        print "posnInCycle",posnInCycle
                        print
                cycle[posnInCycle] = person
                posnInCycle = posnInCycle + 1
                pasInList = second[person]
                if debugg3:
                        print "SECOND",second

                # Changes the Next Choice and checks its ranking against the right most choice of their right most choice
                while True:
                        if debugg3:
                                print "pasinlist",pasInList
                                print "person",person
                        nextChoice = preference[person][pasInList]
                        if debugg3:
                                print "nextchoice",nextChoice
                        pasInList = pasInList + 1
                        if debugg3:
                                print "ranking",ranking[nextChoice][person],"<=","right",rightmost[nextChoice]
                        if(ranking[nextChoice][person] <= rightmost[nextChoice]):
                                break
                        if(pasInList == n+1): # this keeps the loop from going past a usable range incase the previous condition is not met. 
                                break
                second[person] = pasInList - 1
                person = preference[nextChoice][rightmost[nextChoice]]
                if debugg3:
                        print "//person//",person
                        print "//cycleSet//",cycleSet
                        print 
                if(person in cycleSet):
                        break
        lastInCycle = posnInCycle - 1
        tail = []
        for x in cycleSet:
                tail.append(x)
        if debugg3:
                print "posnInCycle",posnInCycle
                print "person",person
                print "cycle post",cycle[posnInCycle]
                print "posnInCycle",posnInCycle
                print
        # this keeps the tail updated to what it needs to be for the Cycle to complete
        while True:
                posnInCycle = posnInCycle - 1
                if debugg3:
                        print "cycle",cycle
                        print "posInCycle",posnInCycle
                        print
                x= cycle[posnInCycle]
                if x in tail:
                        tail.remove(x)
                if(cycle[posnInCycle] == person):
                        break
        firstInCycle = posnInCycle
        if debugg3:
                print"==============================================="

#
# Phase Two reduces the the list of potential partners and shifts the lists accordinglly. 
#

def phaseTwo():
        if debugg4:
                print "=====================Phase Two===================="
        global second
        global cycle
        global leftmost
        global rightmost
        global ranking
        global firstInCycle
        global lastInCycle
        global soln_possible
        for rank in range(firstInCycle, lastInCycle + 1):
                if debugg4:                        
                        print "proposer",proposer
                        print "cycle[rank]",cycle[rank]
                        print "leftmost[proposer]",leftmost[proposer]
                        print "second[proposer]",second[proposer]
                        print "nextChoice",nextChoice
                        print "preference[proposer][leftmost[proposer]]",preference[proposer][leftmost[proposer]]
                        print "rightmost[nextChoice]",rightmost[nextChoice]
                        print "ranking[nextChoice][proposer]",ranking[nextChoice][proposer]
                proposer = cycle[rank]
                leftmost[proposer] = second[proposer]
                second[proposer] = leftmost[proposer] + 1
                nextChoice = preference[proposer][leftmost[proposer]]
                rightmost[nextChoice] = ranking[nextChoice][proposer]
                if debugg4:
                        print "proposer",proposer
                        print "leftmost[proposer]",leftmost[proposer]
                        print "second[proposer]",second[proposer]
                        print "nextChoice",nextChoice
                        print "rightmost[nextChoice]",rightmost[nextChoice]

        rank = firstInCycle

        while(rank <= lastInCycle) and soln_possible:
                proposer = cycle[rank]
                soln_possible = leftmost[proposer] <= rightmost[proposer]
                if debugg4:
                        print "soln_possible =",soln_possible
                rank = rank + 1
        if debugg4:
                print "=================================================="

#
# If the Data loaded in has an Odd number if people this method creates another person, 
# a preference list for them and adds them into everyone elses prefrence list.
#

def oddNumber():
        loadFromFile()
        if debugg5:
                print "====================Odd Number======================="
        global second
        global cycle
        global leftmost
        global rightmost
        global preference
        global ranking
        global n
        w = 0
        if(n % 2 == 1):
                n = n+1
                preference[0].append(-1)
                transferN1 = 0
                transferN2 = 0
                newPerson = n
                test = []
                x = 0
                for x in range(1,n+1):
                        test.append(x)
                newpref = random.sample(test,n-1)
                newpref.insert(0,-1)
                newpref.append(-1)
                preference.append(newpref)
                player = 1
                for player in range(1,n):
                        transferP1 = random.randint(1,n-1)
                        preference[player].insert(transferP1,n)
                for w in range(0,n+1):
                        if debugg5:
                                print preference[w]
        if debugg5:
                print "====================================================="

#
# This fills the lists created at the begining with the appropreate amount of dumby spaces 
# so that it the program can function
#

def generation():
        oddNumber()
        if debugg6:
                print "===================Generation========================"
        global second
        global cycle
        global leftmost
        global rightmost
        global ranking
        global n
        
        x = 0
        y = 0
        w = 1
        for x in range(0,n+1):
                second.append(-1)
        for x in range(0,n+2):
                cycle.append(x)
                leftmost.append(y)
                rightmost.append(y)
                y = y - 1
        if debugg6:
                print "second",second
                print "cycle",cycle
                print "leftmost",leftmost
                print "rightmost",rightmost
        ranks0 = []
        ranks1 =[]
        ranks1.append(0)
        for x in range(1,n):
                ranks1.append(-1)
        ranks1.append(0)
        for x in range(1,n+2):
                ranks0.append(0)
        ranking.append(list(ranks0))
        for w in range(1,n+1):
                ranking.append(list(ranks1))

        for x in range(0,n+1):
                if(x == 0):
                        for y in range(0,n+1):
                                ranking[x][y] = 0
                else:
                        for y in range(0, n):
                                if y == 0 or y == n+1:
                                        ranking[x][y] = 0
                                else:
                                        ranking[x][y] = -1
                ranking[x][n] = 0
        if debugg6:
                print "Ranking in Generation"                                
                for y in range(0,n+1):
                        print ranking[y]
        if debugg6:
                print "========================================================="

#
# This loads the Preferences from an external file and sets them to the preferences in this program
# it also sets N to the amount of people in the grouping
#

def loadFromFile():
        if debugg7:
                print "===============Load From File============================"
        global n
        global preference
        with open('Players Skill Prefs.txt') as f:
                preference = []
                for line in f:
                        line = line.split() # to deal with blank 
                        if line:            # lines (ie skip them)
                                line = [int(i) for i in line]
                                preference.append(line)
        n = len(preference) - 1
        y = 0
        if debugg7:
                print "before Odd Correction"
                for y in range(0,n+1):
                        print preference[y]
        if debugg7:
                print "========================================================="

#
# This is the creates the the actual values of the RAnking Matrix along with being the 'Main' that calls the other methods as needed. 
#

def roommates():
        generation()
        if debugg8:
                print "==============Roommates===================="
        global rank        
        global firstInCycle
        global firstUnmatched
        global second
        global cycle
        global leftmost
        global rightmost
        global ranking
        global n
        if debugg8:
                print "preference"
                for n in range(0,n+1):
                        print preference[n]
                print "second",second
                print "cycle",cycle
                print "leftmost",leftmost
                print "rightmost",rightmost
                print "ranking"
        y=0
        if debugg8:
                for y in range(0,n+1):
                        print ranking[y]
        solnFound = False
        firstUnmatched = 1
        firstInCycle = 1
        i = 1
        # This fills the ranking matrix
        for person in range(1, n+1):
                preference[person][n] = person
                for rank in range(1, n+1):
                        ranking[person][preference[person][rank]] = rank
                leftmost[person] = 1
                rightmost[person] = n
        leftmost[n+1] = 1
        rightmost[n+1] = n 
        if debugg8:
                print "Ranking"
                for y in range(0,n+1):
                        print "rankings for#",y,ranking[y]
                print 
                print "leftmost", leftmost
                print "rightmost",rightmost
                print 
        phaseOne()
        if debugg8:
                print "soln_possible:",soln_possible
                print "Leftmost",leftmost
                print "rightmost",rightmost
                print 
                print "Ranking"
                for y in range(1,n+1):
                        print ranking[y]
                print
                print "second",second
                print 
        for person in range(1,n+1):
                if debugg8:
                        print "left",leftmost[person]
                        print "left",leftmost[person]+1
                        print "second",second[person]
                second[person] = leftmost[person] +1
                if debugg8:
                        print "second v2",second[person]
                        print
        #opperates the three parts of "PHase Two" that reduce and re-assign pairings
        while(soln_possible and not solnFound):
                if debugg8:
                        print "FirstUnmatched before the call",firstUnmatched
                find()
                if firstUnmatched > n:
                        solnFound = True
                        print "SolnFound",solnFound
                else:
                        seek()
                        phaseTwo()
                person = person + 1
        if solnFound:
                f = open("FinalPairs.txt","w+")
                alreadyIn = []
                for person in range(1, n+1):
                        roomie = preference[person][leftmost[person]]
                        if roomie in alreadyIn:
                                pass
                        elif person in alreadyIn:
                                pass
                        else:
                                string1 = str(person)
                                string2 = str(roomie)
                                alreadyIn.append(roomie)
                                alreadyIn.append(person)
                                string3 = string1 + "," + string2 + "\n"
                                f.write(string3)
                                partner.append([person,roomie])
                print "Partner",partner
                f.close()
        else:
                print "<<<<<<<<<<No Solution>>>>>>>>>>"
        if debugg8:
                print "==========================================="
roommates()



























