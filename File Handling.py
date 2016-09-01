# Carlin MacKenzie, 31/08 - 01/09

bikeClasses = []
bikeDictionary = []

# Classes
class Bike():
    def __init__(self, Model=None, Gears=None, Type=None, Price=0):
        self.Model = Model
        self.Gears = Gears
        self.Type = Type
        self.Price = Price

def inputClasses(bikeClasses):
    with open("bikes.txt") as readFile:
        line = readFile.readline().rstrip("\n")
        while line:
            items = line.split(",")

            Model = items[0]
            Gears = items[1]
            Type = items[2]
            Price = items[3]
            bikeClasses.append(Bike(Model, Gears, Type, Price))

            line = readFile.readline().rstrip("\n")
    return bikeClasses

# Dictionaries
def inputDictionaries(bikeDictionary):
    with open("bikes.txt") as readFile:
        line = readFile.readline().rstrip("\n")
        while line:
            items = line.split(",")

            Model = items[0]
            Gears = items[1]
            Type = items[2]
            Price = items[3]

            bikeDictionary.append({"Model": Model, "Gears": Gears, "Type": Type, "Price": Price})
            print(bikeDictionary)
            line = readFile.readline().rstrip("\n")
    return bikeDictionary

inputDictionaries(bikeDictionary)
inputClasses(bikeClasses)

# Display Dictionary
def displayDict():
    for k in range(len(bikeDictionary)):
        temp = ""
        for l in range(len(bikeDictionary[k])):
            temp += (bikeDictionary[k+1][l] + " ")
        print(temp)  # output

displayDict()
