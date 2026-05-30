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


    