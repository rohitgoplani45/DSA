#Find First Occurrence
arr = [4, 7, 2,5]
target = 9
value=-1
for i in range(len(arr)):
    if arr[i]==target:
        value=i
        break

print(value)

#second largest element

def second_largest(arr):
    maximum=arr[0]
    for i in range(len(arr)):
        if arr[i]>maximum:
            maximum=arr[i]

    second_largest=float('-inf')
    for j in arr:
        if j<maximum and j>second_largest:
            second_largest=j

    if second_largest == float('-inf'):
        return -1

    return second_largest 
    pass

#frequency counting
def count_occurrences(arr, target):
    count = 0
    for i in range(len(arr)):
        count += (arr[i]==target)
    return count
    pass


#Given an array, count how many elements are greater than 5.
def count_greater_than_five(arr):
    count=0
    for i in range(len(arr)):
        if arr[i]>5:
            count += 1
    return count
    pass



#Find the index of the largest element in the array.
def index_of_largest(arr):
    max_number=float('-inf')
    value=-1
    for i in range(len(arr)):
        if arr[i]>max_number:
            max_number=arr[i]
            value=i
    return value
    pass



    