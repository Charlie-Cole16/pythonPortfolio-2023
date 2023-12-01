# List of numbers that we need to find
lNumberList = [1,5,7,67,89,100,122,155,178,190]

#A linear search algorithm may typically use an ordered list, however this is not a requirement within this algorithm

#Create an input to ask the user what they want to find:
iNumberInput = int(input("Enter in a number that you want to find: "))

#We are gonna create what is known as a "Flag", more on this later:
bFound = False

#Create a FOR which goes through each of the numbers in sequence: 
for iCount in range(len(lNumberList)):
    #Check if the lNumberInput matches what is in the list:
    if iNumberInput == lNumberList[iCount]:
        print ("We have found the number, this is in position", iCount)
        bFound = True
if bFound == False:
    print (iNumberInput, "was not found")
