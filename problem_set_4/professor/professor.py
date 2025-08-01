import random
"""
single digit = 1-10
double=
"""

def main():
    level=get_level()

    tries=0   #tracks how many equations given
    score=0   #tracks the score

    #ensures 10 questions are asked
    while  tries <10 :

         x=generate_integer(level)   #random x value
         y=generate_integer(level)   #random y value
         correct_answer= int(x+y)

         attempt = 0 #tracks number of attempts

         #tracks number of attempts
         while attempt < 3:
            try:
                user_answer = int(input(f"{x} + {y} = ")) #prompt user input
                if user_answer == correct_answer:
                    score += 1
                    break  # exit retry loop
                else:
                    print("EEE")
                    attempt += 1
            except ValueError:
                print("EEE")
                attempt += 1

         if attempt == 3:
            print(f"Correct answer: {correct_answer}")

         tries += 1

    print(f"Score: {score}")


def get_level():

    while True:
      try:
        level=int(input("Level: "))
        if level in (1, 2, 3):
          return level
      except ValueError:
        pass




def generate_integer(level):
     try:
         level=int(level)
         if level ==1:
            return random.randint(0,9)

         elif level==2:
          return random.randint(10,99)

         elif level ==3:
          return  random.randint(100,999)
         else:
          raise ValueError
     except ValueError:
         pass


#def generate_problems(x,y):




if __name__ == "__main__":
    main()
