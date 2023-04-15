
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
            print(UsrInput)
            if UsrInput == test[j]: 
                print(UsrInput)
                j = length
                i = length
            j += 1
    return UsrInput

test = ["1", "2"]
input = GetUsrIn(test)
print(input)