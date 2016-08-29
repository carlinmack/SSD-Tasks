# Carlin MacKenzie, 29/08
initArray = [5, 3, 10, 24, 26, 1, 7]

# Insertion
array = list(initArray)
for l in range(1, len(array)):
    index = l
    value = array[l]
    while index > 0 and value < array[index-1]:
        temp = array[index]
        array[index] = array[index-1]
        array[index-1] = temp
        index -= 1
print(array)

# Selection
array = list(initArray)
for k in range(len(array)):
    minVal = k
    for j in range(k+1, len(array)):
        if array[minVal] > array[j]:
            minVal = j
    temp = array[k]
    array[k] = array[minVal]
    array[minVal] = temp
print(array)

# Bubble
array = list(initArray)
swap = True
while swap:
    swap = False
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            swap = True
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp
print(array)

# Quick Sort


print(initArray)
