#Import libraries
import pandas as pd
import sys

#Function to ask user for input
def GetUsrIn(test):

    #Creates variables to use for the while loop
    i = 0
    length = len(test)

    #Creates a while loop that check's the user's input for validity
    while i < length:
        
        #Prints statements and asks user for input
        print("\nPlease enter your preferred genre of music from this list below:")
        print("hip hop, pop, rap, edm, indie, country, rock, r&b")
        print("If the genre is not found, you will be asked to enter a new one.")
        UsrInput = input("Enter a genre or press q to quit: ")

        #Creates an if statement that checks if the user enters 'q' to quit
        if UsrInput == "q":
            sys.exit(0)
        j = 0

        #Creates another nested while loop that compares the user's input to the genre parameter
        #and will continue to ask the user genre;s until a valid genre has been entered
        while j < length:
            if UsrInput == test[j]: 
                print(UsrInput)
                j = length
                i = length
            j += 1
    return UsrInput

#Calls and creates parameters for the function we created above
genres = ["hip hop", "pop", "rap", "edm", "indie", "country", "rock", "r&b"]
usergenre = GetUsrIn(genres)

# DAY ONE
#Separates the csv into readable rows and columns for day 1
coachlineup = pd.read_csv("Coachella_Day_1.csv", sep = ",")

#Sorts and prints the lineup per suggested genre for day 1
sortbyGenre = coachlineup[coachlineup["Genre"]==usergenre]
print("\nDay 1's lineup: \n", sortbyGenre)

#Separates the data into lists
listNames = sortbyGenre['Artist'].tolist()
listStartTime = sortbyGenre['Start'].tolist()
listEndTime = sortbyGenre['End'].tolist()

#Reverses the order of the lists to fix time error
finlistNames = listNames.reverse()
finlistStartTime = listStartTime.reverse()
finlistEndTime = listEndTime.reverse()


#DAY TWO
#Separates the csv into readable rows and columns for day 2
coachlineup2 = pd.read_csv("Coachella_Day_2.csv", sep = ",")

#Sorts and prints the lineup per suggested genre for day 2
sortbyGenre2 = coachlineup2[coachlineup2["Genre"]==usergenre]
print("\nDay 2's lineup: \n", sortbyGenre2)

#Separates the data into lists
listNames = sortbyGenre2['Artist'].tolist()
listStartTime = sortbyGenre2['Start'].tolist()
listEndTime = sortbyGenre2['End'].tolist()

#Reverses the order of the lists to fix time error
finlistNames = listNames.reverse()
finlistStartTime = listStartTime.reverse()
finlistEndTime = listEndTime.reverse()


#DAY THREE
#Separates the csv into readable rows and columns for day 3
coachlineup3 = pd.read_csv("Coachella_Day_3.csv", sep = ",")

#Sorts and prints the lineup per suggested genre for day 3
sortbyGenre3 = coachlineup3[coachlineup3["Genre"]==usergenre]
print("\nDay 3's lineup: \n", sortbyGenre3)

#Separates the data into lists
listNames = sortbyGenre3['Artist'].tolist()
listStartTime = sortbyGenre3['Start'].tolist()
listEndTime = sortbyGenre3['End'].tolist()

#Reverses the order of the lists to fix time error
finlistNames = listNames.reverse()
finlistStartTime = listStartTime.reverse()
finlistEndTime = listEndTime.reverse()
