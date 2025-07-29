vowels=["A","E", "I" ,"O", "U", "a","e", "i", "o" ,"u"]  #list containing all the vowels
string_char=[]    #list to contain characters that are nt vowels
string=input("Input:" )

for v in string:                     #loop through  characters in input
    if  v not in vowels:               #check if character is not in vowel list
        string_char.append(v)            # add char to a new list
    new_string="".join(string_char)
    
print(new_string)
