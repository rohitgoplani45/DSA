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



#Given a string, count how many characters it contains.
def count_characters(s):
    count=0
    for i in s:
        count+=1
    return count
    pass



#Count how many times the character 'a' appears in a string.
def count_a(s):
    count=0
    for i in s:
        if i=="a":
            count+=1
    return count
    pass

#Count vowels
def count_vowels(s):
    count=0
    for i in s:
        if i in "aeiou":
            count+=1

    return count 
    
    pass

#Given a string, create and return its reverse.
def reverse_string(s):
    s2=""
    for i in range(len(s)-1,-1,-1):
        s2=s2+s[i]
    return s2
    pass

#Return True if the string is a palindrome, otherwise False.
def is_palindrome(s):
    s2=""
    answer=""
    for i in range(len(s)-1,-1,-1):
        s2=s2+s[i]
    return s==s2
    pass  