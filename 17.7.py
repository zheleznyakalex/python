def find(array, element):
    for i, a in enumerate(array):
        if a == element:
            return i
    return False

array = list(map(int, input().split()))
element = int(input())

print(find(array, element))

def count(array, element):
    count = 0
    for a in array:
        if a == element:
            count +=1
        return count