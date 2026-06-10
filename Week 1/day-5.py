#Return the number of unique elements in the array.
def count_unique(arr):
    s=set()
    for i in arr:
        s.add(i)
    return len(s)
    pass


def count_unique(arr):
    s=set()
    unique_char=0
    for i in arr:
        if i in s:
            pass
        if i not in s:
            s.add(i)
            unique_char += 1
    return unique_char
    pass

#Check if array contains any duplicate value
def contains_duplicate(arr):
    s=set()
    duplicate_value=False
    for i in arr:
        if i not in s:
            s.add(i)
        elif i in s:
            duplicate_value=True
            break
    return duplicate_value
    pass

def contains_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
return False


#Return True if all elements in the array are unique.
def all_unique(arr):
    uniq_elem=True
    s=set()
    for i in arr:
        if i not in s:
            s.add(i)
        elif i in s:
            return False
    return True
    pass

def all_unique(arr):
    s= set()
    for i in arr:
        if i in s:
            return False

        s.add(i)

    return True
    
#Return an array containing only the unique elements in their first appearance order.
def remove_duplicates(arr):
    s=set()
    result=[]
    for i in arr:
        if i not in s:
            s.add(i)
            result.append(i)
    return result
    pass

#Return the first duplicate value in the array.
def first_duplicate(arr):
    s=set()
    for i in arr:
        if i in s:
            return i
        s.add(i)
    return None
    pass

    
    