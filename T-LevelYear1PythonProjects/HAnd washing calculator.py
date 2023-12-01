iMonthDays = 30 #~~How many days in a month

#~~User Inputs~~#
iDays = int(input("How many times do you wash your hands in a day?: "))
iMonths = int(input("How many months did you follow this routine for?: "))

#~~Main_Function~~#

def wash_hands(Days, Months):
    Time = ((Days * (Months * iMonthDays)) * 21) / 60 #~~ Calculating how long you spend washing your hands

    sMinutes = ""
    sSeconds = ""

    sTime = str(Time)
    bwasDecimal = False

    for v in range(len(sTime)): #~~ Gathering decimal to calculate seconds
        if v != 0:
            if sTime[(v*-1)] != ".":
                print(sTime[(v*-1)])
                sSeconds = sSeconds + sTime[(v*-1)]
            else:
                bwasDecimal = True
                break
    
    iSeconds = int(sSeconds) * 6 , "Seconds #~~Calculating seconds"

    for v in range(len(sTime)): #Gathering minuets to seperate from decimal point
        if sTime[v] == ".":
            break
        else:
            sMinutes = sMinutes+ sTime[v]
    
    iMinutes = int(sMinutes) #~~ Converting the string minutes to an integer

    print(str(iMinutes) , "Minutes and" , int(sSeconds) * 6 , "Seconds")

wash_hands(iDays, iMonths)
