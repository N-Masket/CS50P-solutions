"""
1.if n is a string
2. if n is -
"""
import random
import sys

def main():
     level=get_level()
     guess_num(level)






#function to generate integer between 1 and n
def guess_num(n):

        random_num=random.randint(1,n)  #random number to be generated
        while True:
            try:
                guess=int(input("Guess: "))   #prompt user to guess


                if guess<=0:
                    continue

                     #check if guess is small
                if guess<random_num:
                        print("Too small!")
                        guess=int(input("Guess: "))

                        #check if guess is large
                elif guess>random_num:
                        print("Too large!")
                        guess=int(input("Guess: "))

                        #check if guess matches random number
                elif guess==random_num:
                            print("Just Right!")
                            break

            except ValueError:
               pass



#function to get level
def get_level():

  while True:
        try:
            #prompt user for number and convert to integer
            number=int((input("Level: ")))

            #ask user for num as long as input negative and not num
            if number <0:
                number=int(input("Level: "))
            else:
                return number

        except :
            pass   #keep asking for input


main()
