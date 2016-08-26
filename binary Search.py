# Carlin MacKenzie, 23/08 - 24/08

array = [1, 3, 6, 8, 10, 12, 14, 18, 22, 23, 44, 49, 55, 60, 71, 79, 83, 90, 99, 111, 120, 323, 478, 576, 930, 978, 1024, 1666, 2134, 3423, 7568, 7777]

def binarySearch():

    # init variables
    found = False
    start = 0
    end = len(array) - 1
    compar = 0
    ind = 0
    term = int(input("input number to search: "))


    while start <= end and found == False:
        mid = (start+end)//2
        print(mid, array[mid])
        compar += 1
        if array[mid] == term:
            found = True
            ind = mid
        elif array[mid] < term:
            start = mid + 1
        else:
            end = mid - 1

    if found == True:
        print("found at index: " + str(ind))
        print("comparisons: " + str(compar))
    else:
        print("not found, comparisons: " + str(compar))

binarySearch()
