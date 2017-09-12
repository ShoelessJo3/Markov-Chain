import time
import datetime
import json
import pickle

import sys
import os


#ShoelessJoe 2/14/17
#This was created on a raspberry pi and used for Joe's twitter bot @AI_Shakespeare
#MarkovChain 2.0 ShoelessJoe 9/11/17
#Added a way to store and load the array data with the pickle library

#The purpose of this program is to execute a Markov Chain
#The markovLoader program stores the distribution of each state in a 2D array.
#The markovChain program executes the state-to-state transition and returns the path

import random
import os
RAP_LIMIT = 200 #max words it can generate
arrayMarkov = []
MAX_CHARACTERS = 5000
path = 'pickle_test.data'


print("Program initialized, beginning Stage 1") #annoying initialization message


def markovRecursive(array, num, count):
    #this recursive method does the state-to-state transition.  At the end of the recursion it returns the path as a concatenated string
    count += 1
    found = False
    numWords = len(array[num]) - 1 #prints number of words in slot (-1 for seed word)
    word = "l"

    if numWords > 0: #if no tag words then end statement
        found = True
        randNum = random.randint(1,numWords) #select a random word in the array, probability of choosing increases as repeated words are added to a single variable

        word = array[num][randNum];
        num = 0

        
    

   
        for x in range(0, len(array)):
            if array[x][0] == word:
                num = x
        #find next number in list, num = index of next number        


    if found == False or count >= RAP_LIMIT: #count prevents recursive from going infinite
        return "." #this means we are at the end, there is nothing to relate to the word, returns a space
    else:
        if count > 1: #not at start of sentence
            word = " " + word #adds a space before word, this allows the recursive statement to end on a simple period
        
        return word + markovRecursive(array, num, count) #returns recursive statement with progressive count



with open(path, 'r') as f: #pickle_test.data is the path to the data loaded by markovloader.py
    	arrayMarkov = pickle.load(f)

#this function loads the pickle file created by markovLoader.py




for x in range(0,100):#this will create 100 different paths and output them


    while True:
        numWords = len(arrayMarkov)
        randNum = random.randint(0,numWords) - 1
    
        if len(arrayMarkov[randNum]) > 1:
            break
                #purpose of this statement is to find a word that has something related to it, so the sentence will be at least 1 word
    
                #seeds markov recursive at random number
    #while True:
    #                
    #    song = markovRecursive(arrayMarkov, randNum, 0)
    #    numLen = len(song)
    #    if numLen < MAX_CHARACTERS:
    #        break
    #This generates paths until it finds one less than a certain # of characters
    #this is useful for tweets, since you can set it to be less than 140 characters

    song = markovRecursive(arrayMarkov, randNum, 0)
       #this creates a path through the array and returns as a string 


    song = song.capitalize()
       #function capitalizes first letter in the sentence, for grammar purposes
    song = song.replace(' i ', ' I ') #capitalize I the pronoun, for grammar porpoises
                    
    print(song)

    os.system('flite -voice kal16 -t " t t ' + song + '"') #this line uses the Flite text-to-speech library to read the path.  You can download this library online
    #else just comment it out

       
 


           
                              



