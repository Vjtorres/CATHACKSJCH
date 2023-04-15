#Import csv files
import pandas as pd
BBHot = pd.read_csv('billboard_hot_100.csv', sep = ",")

#print("\nInput CSV file = \n", BBHot)

#Asks user for genre input
usergenre = input("\nPlease enter your preferred genre of music (all lowercase).\n")

#Sorts and prints the billboard file to meet genre requirements
sortbyGenre = BBHot[BBHot["Genres"]==usergenre]
print("\nSorted CSV by genre = \n", sortbyGenre)

#Sorts and prints the names of the genre sorted list by name
sortbyName = sortbyGenre.loc[:,"Artist Name(s)"]
print("\nSorted CSV by name from genre sort = \n", sortbyName)
