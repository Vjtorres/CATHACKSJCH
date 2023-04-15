
def GetUsrIn(test):
    i = 0
    length = len(test)
    while i < length:
        i = 0
        UsrInput = input("Enter a genre or press q to quit: ")
        if UsrInput == "q":
            break
        j = 0
        while j < length:
            if UsrInput != test[j]: 
                i+=1 
            j += 1
    return UsrInput

test = ["10", "11"]
UsrIn = GetUsrIn(test)
print(UsrIn)

    