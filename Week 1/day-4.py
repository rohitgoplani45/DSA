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