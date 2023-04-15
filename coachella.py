#Import csv files
import pandas as pd
import sys
coachlineup = pd.read_csv('CoachLineupD1.csv', sep = ",")

#Function to ask user for input
def GetUsrIn(test):
    i = 0
    length = len(test)
    while i < length:
        i = 0
        print("\nPlease enter your preferred genre of music from this list below:")
        print("hip hop, pop, rap, edm, indie, country, rock, r&b")
        print("If the genre is not found, you will be asked to enter a new one.")
        UsrInput = input("Enter a genre or press q to quit: ")
        if UsrInput == "q":
            sys.exit(0)
        j = 0
        while j < length:
            if UsrInput == test[j]: 
                print(UsrInput)
                j = length
                i = length
            j += 1
    return UsrInput
genres = ["hip hop", "pop", "rap", "edm", "indie", "country", "rock", "r&b"]

usergenre = GetUsrIn(genres)
print(usergenre)




# print("\nPlease enter your preferred genre of music from this list below:")
# usergenre = input("hip hop, pop, rap, edm, indie, country, rock, r&b.\n")


#Sorts and prints the billboard file to meet genre requirements
sortbyGenre = coachlineup[coachlineup["Genre"]==usergenre]
print("\nSorted CSV by genre = \n", sortbyGenre)

#Separates the data into lists
listNames = sortbyGenre['Artist'].tolist()
listStartTime = sortbyGenre['Start'].tolist()
listEndTime = sortbyGenre['End'].tolist()

#Reverses the order of the lists to fix time error
finlistNames = listNames.reverse()
finlistStartTime = listStartTime.reverse()
finlistEndTime = listEndTime.reverse()

print(listNames)
print(listStartTime)
print(listEndTime)