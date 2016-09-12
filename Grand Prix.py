# Carlin MacKenzie, 12/09

driverDictionary = []
def inputDictionaries(driverDictionary):
    with open("racing.csv") as readFile:
        line = readFile.readline().rstrip("\n")
        while line:
            items = line.split(",")

            Driver = items[0]
            Team = items[1]
            Time = items[2]
            Points = items[3]

            driverDictionary.append({"Driver": Driver, "Team": Team, "Time": Time, "Points": Points})
            line = readFile.readline().rstrip("\n")
    return driverDictionary

def userInput():
    for i in range(len(driverDictionary)):
        temp = input("Race time for " + str(driverDictionary[i]["Driver"]) + " is... ")
        driverDictionary[i]["Time"] = temp

def sortDrivers():
    swap = True
    while swap:  # runs until it is sorted
        swap = False  # resets flag
        for i in range(len(driverDictionary) - 1):  # traverses whole driverDictionary array
            if driverDictionary[i]["Time"] > driverDictionary[i + 1]["Time"]:  # if values are unsorted
                swap = True  # triggers flag
                # swaps the unsorted adjacent values
                temp = driverDictionary[i]
                driverDictionary[i] = driverDictionary[i + 1]
                driverDictionary[i + 1] = temp

def assignPoints():
    driverDictionary[0]["Points"] = 25
    driverDictionary[1]["Points"] = 18
    driverDictionary[2]["Points"] = 15

def writeValues():
    temp = "Driver".ljust(22) + "Team".ljust(15) +"Time".ljust(10) + "Points".ljust(10)
    for j in range(len(driverDictionary)):
        temp += driverDictionary[j]["Driver"].ljust(22)
        temp += driverDictionary[j]["Team"].ljust(15)
        temp += str(driverDictionary[j]["Time"]).ljust(10)
        temp += str(driverDictionary[j]["Points"]).ljust(10)

    with open("newfile.txt", "a") as writeFile:
        writeFile.write(temp)
        print("File updated!")
    
# -------Main-------
inputDictionaries(driverDictionary)
userInput()
sortDrivers()
assignPoints()
writeValues()
