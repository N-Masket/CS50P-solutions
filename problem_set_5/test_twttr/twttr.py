vowels=["A","E", "I" ,"O", "U", "a","e", "i", "o" ,"u"]  #list containing all the vowels
   #list to contain characters that are nt vowels


def main():
    string=input("Input:" )
    print(shorten(string))


def shorten(word):
    string_char=[]
    for char in word:                     #loop through  characters in input
        if  char  not in vowels:               #check if character is not in vowel list
            string_char.append(char)            # add char to a new list
        new_string="".join(string_char)
    return new_string


if __name__=="__main__":
   main()

"""
initial program solution in problem set 2

vowels=["A","E", "I" ,"O", "U", "a","e", "i", "o" ,"u"]  #list containing all the vowels
string_char=[]    #list to contain characters that are nt vowels


for v in string:                     #loop through  characters in input
    if  v not in vowels:               #check if character is not in vowel list
        string_char.append(v)            # add char to a new list
    new_string="".join(string_char)

print(new_string)

"""
