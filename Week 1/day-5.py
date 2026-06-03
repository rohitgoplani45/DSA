#Given a dictionary, return the age of the person.
def get_age(person):
    age_of_person=0
    for key in person:
        if key == "age":
            age_of_person=person[key]
    return age_of_person
    pass

def get_age(person):
    return person["age"]
    pass


# add city indore to the dictionary and return dictionary
def add_city(person):
    person["city"]="Indore"
    return person
    pass

#Create a frequency dictionary for an array.
def frequency_count(arr):
    freq_dict={}
    for i in range(len(arr)):
        if arr[i] in freq_dict:
            freq_dict[arr[i]]+=1
        else:
            freq_dict[arr[i]]=1
    return freq_dict
    
#Given a string, return a dictionary containing the frequency of each character.
def char_frequency(s):
    freq_dict={}
    for ch in s:
        if ch in freq_dict:
            freq_dict[ch]+=1
        else:
            freq_dict[ch]=1
    return freq_dict
    pass

#Given a string, return the character that appears the most times.
def char_frequency(s):
    freq_dict={}

    #Phase 1
    for ch in s:
        if ch in freq_dict:
            freq_dict[ch]+=1
        else:
            freq_dict[ch]=1

    #Phase 2
    max_count=0
    max_count_char=""
    for key in freq_dict:
        if freq_dict[key]>max_count:
            max_count=freq_dict[key]
            max_count_char=key
    return max_count_char

    pass

#Rewrite frequency counting using .get().
def frequency_count(arr):
    freq_dict={}
    for number in arr:
        freq_dict[number]= freq_dict.get(number,0)+1
    return freq_dict
    pass


#Return the first character that appears exactly once.
def first_non_repeating(s):
    freq_dict={}
    for i in s:
        freq_dict[i]= freq_dict.get(i,0)+1
    ch=""
    for m in s:
        if freq_dict[m]==1:
            ch=m  
            break
    return ch  
    pass

#Rewrite first_non_repeating(s) correctly.
def first_non_repeating(s):
    freq_dict={}
    for i in s:
        freq_dict[i]= freq_dict.get(i,0)+1
    ch = None
    for m in s:
        if freq_dict[m]==1:
            ch=m
            break
    return ch
    pass

