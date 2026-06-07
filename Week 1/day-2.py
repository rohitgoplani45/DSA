# Sum of array elements
arr=[1,3,5,7,9]
total=0
for i in arr:
    total+=i
print(total)

#even number count
arr=[1,3,2,8,54,5,7,9]
count=0
for i in arr:
    if i%2==0:
        count+=1
print(count)

#odd numbers count
arr=[1,3,2,8,54,5,7,9]
count=0
for i in arr:
    if i%2!=0:
        count+=1
print(count)

#maximum number
arr=[1,3,2,8,54,5,7,9]
maximum=arr[0]
for i in range(len(arr)):
    if arr[i]>maximum:
        maximum=arr[i]
print(maximum)

#Minimum element
arr=[1,3,2,8,54,5,7,9]
minimum = arr[0]
for x in arr:
    if x < minimum:
        minimum = x
print(minimum)


#sum of positive numbers
arr=[1,3,2,8,54,5,7,9]
total=0
for i in arr:
    if i%2==0:
        total+=i
print(total)

#reverse array using loop
arr=[1,3,2,8,54,5,7,9]
reversed_arr = []

for i in range(len(arr)-1, -1, -1):
    reversed_arr.append(arr[i])

print(reversed_arr)



#2nd largest number
arr=[1,3,2,8,54,5,7,9]
maximum=arr[0]
for i in range(len(arr)):
    if arr[i]>maximum:
        maximum=arr[i]
print(maximum)

second_largest=arr[0]
for j in arr:
    if j<maximum and j>second_largest:
        second_largest=j
print(second_largest)


#Running sum of 1D array
arr=[1,3,2,8,54,5,7,9]
i=1
while i < len(arr):
    arr[i]=arr[i]+arr[i-1]
    i+=1

print(arr)

#1295. Find Numbers with Even Number of Digits
new=[12,154,1548,15987,4658]
elements=0
for i in new:
    if len(str(i))%2==0:
        elements+=1
print(elements)



#1672. Richest Customer Wealth
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
