# Carlin MacKenzie, 29/08
array = [5, 3, 10, 24, 26, 1, 7]

# Insertion

# Selection

# Bubble
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
