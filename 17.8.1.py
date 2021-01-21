array = [2, 3, 1, 4, 6, 5, 9, 8, 7]


for i in range (len(array)):
    idx_min = i
    count += 1
    for j in range (i, len(array)):
        if array[j] < array[idx_min]:
            count += 1
            idx_min = j
            count += 1
    if i != idx_min:
        array[i], array[idx_min] = array[idx_min], array[i]
        count += 1

print(array)
print(count)