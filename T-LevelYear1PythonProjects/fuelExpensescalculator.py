#~~User inputs~~#
sFuelType = input("What fuel type do you use?(Petrol (p) Deisel(d)): ")
iEngineCap = float(input("Please input your engine capcity:" ))
iDistance = float(input("please input the distance (in miles) you have travelled: "))

#~~Main Functions~~#

def Calc_Expenses(FuelType, EngineSize, DistanceTravelled): #~~ Calculation Function
    if sFuelType.lower() == "p": #~~ Checking fuel type
        if iEngineCap <= 1.6: #~~ Checking engine capacity
            return (25 * DistanceTravelled) / 100 #~~ Calculation (Price x Distance Travelloed divided by 100)
        elif iEngineCap >1.6: #~~ Checking engine capacity
            return (32 * DistanceTravelled) / 100 #~~ Calculation (Price x Distance Travelled divided by 100)
    elif sFuelType.lower() == "d": #~~ Checking fuel type
        if iEngineCap <= 1.5: #~~ Checking engine capacity
            return (29 * DistanceTravelled) / 100 #~~ Calculation (Price x Distance Travelled divided by 100)
        elif iEngineCap > 1.5: #~~ Checking engine capacity
            return (36 * DistanceTravelled) / 100 #~~ Calculation (Price x Distance Travelled divided by 100)
        
print(("£")Calc_Expenses(sFuelType, iEngineCap, iDistance)) #~~Displaying expenses
