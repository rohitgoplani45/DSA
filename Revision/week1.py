#Given an integer array arr, return True if any value appears at least twice.
def contains_duplicate(arr):
    return not(len(arr)=len(set(arr)))
    pass


def contains_duplicate(arr):
    s=set()
    for i in arr:
        if i in set():
            return True
        s.add(i)
    return False
    pass


#Given two strings s and t, return True if t is an anagram of s.
def is_anagram(s, t):
    r={}
    n={}
    for i in s:
        r[i] = r.get(i, 0) + 1
    for i in t:
        n[i] = n.get(i, 0) + 1
    return r==n
    pass


#Given an array nums and a target, return the indices of two numbers whose sum equals the target.
def two_sum(nums, target):
    req_dict={}
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
    return False
    pass

def two_sum(nums, target):
    req_dict={}
    needed_number=float('-inf')
    for i in range(len(nums)):
        needed_number=target-nums[i]
        if needed_number in req_dict:
            return (req_dict[needed_number] , i)
        else:
            req_dict[nums[i]]=i
    return False
    pass






Rule to Remember
Uses extra data structure
seen = set()
freq = {}
result = []

Usually:

O(n) space

#Uses only a few variables
i
j
count
maximum

Usually:

O(1) space


Brute force: Compare every pair using nested loops.

Time Complexity: O(n²)

Space Complexity: O(1)