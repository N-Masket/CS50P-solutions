#function to find the first uppercase letter
def check_uppercase_letter(string):
   chars=[]                     #creates a list of chars in string
   for i in string:
        while i.islower():          #checks if char is lowercase
            chars.append(i)
            break
        if i.isupper():
         i=i.lower()
         chars.append('_')
         chars.append(i)
   snake_case="".join(chars)
   print("snake_case",snake_case)


def main():
   variable=input("camelCase: ")
   check_uppercase_letter(variable)

main()
