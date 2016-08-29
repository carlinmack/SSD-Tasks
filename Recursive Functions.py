# Carlin MacKenzie, 25/08 -

# Fibonacci - iterative
prompt = int(input("range: "))  # asks for a number of sequence to go up to
digit1 = 0 
digit2 = 1
fibsum = 1
print("0")
for counter in range(prompt-1):  # iterates until it reaches the range
    print(fibsum)
    fibsum = digit1 + digit2  # calculates new value
    digit1 = digit2  # updates variables
    digit2 = fibsum

# Fibonacci - recursion
def fibonnaci(n):
    if n < 2:
        return n  # if the value asked for is 0 or 1, return them
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)  # finds the next lowest value

for counter in range(prompt):
    print(fibonnaci(counter))  # asks it to find the counter-th term of fibonnaci

# Factorial - iterative
factTemp = 1
for count in range(1, prompt+1): #iterates up to the total prompted
    if count != 0: factTemp *= count  # as long as it's not zero it will multiply the temp value with the next number
    print(factTemp)

# Factorial - recursive
def factorial(m):
    return 1 if m == 1 else m * factorial(m-1)  # uses 1 as the exit condition to start going back up

for counter2 in range(1, prompt+1):  # requests each value up to 100
    print(factorial(counter2))

# Binary Search - iterative
# init variables
array = [1, 3, 6, 8, 10, 12, 14, 18, 22, 23, 29, 41, 44, 49, 55, 60, 71, 79, 83, 90, 99, 111, 120, 323, 478, 576, 675, 691, 930, 978]
term = int(input("input number to search: "))

def iterativeBinarySearch():
    found = False
    start = 0
    end = len(array) - 1
    ind = 0
    while start <= end and found == False:
        mid = (start+end)//2
        if array[mid] == term:
            found = True
            ind = mid
        elif array[mid] < term:
            start = mid + 1
        else:
            end = mid - 1

    if found == True:
        print("found at index: " + str(ind))
    else:
        print("item not found")

iterativeBinarySearch()

# Binary Search - Recursive
def recursiveBinarySearch(begin, final):
    mid = (begin + final) // 2
    if array[mid] == term:
        return "found at index: " + str(mid)
    elif array[mid] < term:
        return recursiveBinarySearch(mid+1, final)
    else:
        return recursiveBinarySearch(begin, mid-1)

#print(recursiveBinarySearch(0, len(array)))
