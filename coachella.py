#Import csv files
import pandas as pd
coachlineup = pd.read_csv('CoachLineupD1.csv', sep = ",")

#Asks user for genre input
print("\nPlease enter your preferred genre of music from this list below:")
usergenre = input("hip hop, pop, rap, edm, indie, country, rock, r&b.\n")


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

print("\n", listNames)
print("\n", listStartTime)
print("\n", listEndTime)