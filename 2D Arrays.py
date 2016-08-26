# Carlin MacKenzie, 18/08/16 - 21/08/16

import random

# task 1
rows = 3
row = ""
columns = 4
Alist = [[0]*columns for i in range(rows)]

for i in range(rows):
    for j in range(columns):
        Alist[i][j] = random.randint(1,9)

# display
for i in range(rows):
    for j in range(columns):
        row += str(Alist[i][j])+ " "
    print(row)
    row = ""

# task 2
budget = [[0]*12 for i in range(15)]
print(budget)

# task 3
array = [[8, 2, 6, 5], [6, 3, 1, 0], [8, 7, 9, 6]]

# search
for k in range(0, 3):
    for l in range(0, 4):
        if array[k][l] == 6:
            print("(" + str(k) + ", " + str(l) + ")")

# task 4
grid = [[0]*9 for i in range(9)]

grid[6][7] = 7
print(grid)

# task 5
readFile = open("testscores.txt", "r")

# processes first line differently by using it to define variables
line = readFile.readline().rstrip("\n")
items = line.split(",")  # splits the line into an array
rows = int(items[0])
cols = int(items[1])

# initialise arrays
scores = [[0]*cols for i in range(rows+1)]
names = []

# for the rest of the program
for h in range(rows+1):
    line = readFile.readline().rstrip("\n")
    items = line.split(",")  # splits the line into an array
    names.append(items[0])  # adds the first item to the names array
    for count in range(1, cols+1):
        scores[h][count-1] = items[count]  # adds score to 2D array

# display
for k in range(rows):
    temp = ""
    temp += (names[k+1] + ": ")  # adds "name: " to array
    for l in range(cols):
        temp2 = round((int(scores[k+1][l]) / int(scores[0][l]) * 100), 0)  # gets percentage
        temp2 = str(temp2)[:-2]  # removes trailing .0
        temp += (temp2 + "% ")  # formats as a percentage
    print(temp)  # output
