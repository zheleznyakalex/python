array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

count = 0

for i in range (len(array)):
    idx_min = i
    for j in range (i, len(array)):
        if array[j] < array[idx_min]:
            count += 1
            idx_min = j
    if i != idx_min:
        array[i], array[idx_min] = array[idx_min], array[i]



for i in range(len(array)):
    idx_max = i
    for j in range(i, len(array)):
        if array[j] > array[idx_max]:
            idx_max = j
    if i != idx_max:
        array[i], array[idx_max] = array[idx_max], array[i]

print(array)
print(count)