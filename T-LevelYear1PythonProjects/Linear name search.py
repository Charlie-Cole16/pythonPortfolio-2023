lNameList = ["Alix", "James", "Tyler", "Mel", "Charlie", "Lucas", "Lesley", "Steve", "Mike", "Lynn","Colin"]

iNameInput = input("Enter a name you would like to find: ")


bFound = False

for iCount in range(len(lNameList)):
    if iNameInput == lNameList[iCount]:
        print ("We have found the name that was inputted at postion", iCount)
        bFound = True
if bFound == False:
    print(iNameInput, "was not found")

