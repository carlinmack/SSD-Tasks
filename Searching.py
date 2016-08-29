# Carlin MacKenzie, 29/08
array = [5, 3, 10, 24, 26, 1, 7]

# Insertion
for l in range(1, len(array)):
    index = l
    value = array[l]
    while index > 0 and value < array[index-1]:
        temp = array[index]
        array[index] = array[index-1]
        array[index-1] = temp
        index -= 1

# Selection
# minVal = [array[0], 0]
# for k in range(len(array)):
#     for j in range(1, len(array)):
#         if minVal[0] > array[j]:
#             minVal[0] = array[j]
#             minVal[1] = j
#     temp = array[k]
#     array[k] = minVal[0]
#     minVal[1] = temp

# Bubble
# swap = True
# while swap:
#     swap = False
#     for i in range(len(array)-1):
#         if array[i] > array[i+1]:
#             swap = True
#             temp = array[i]
#             array[i] = array[i+1]
#             array[i+1] = temp

# Quick Sort
print(array)
