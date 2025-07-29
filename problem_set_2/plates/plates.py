def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#check if plate is num n letters only
def is_valid(s):
    if s.isalnum():
        if not minmax(s):
            return False
        if not isletter(s):
            return False
        if not check_num_position(s):
            return False
        return True
    return False


#check if plate has a min of 2 and max 6 characters
def minmax(s):
          return len(s)>2 and len(s)<7

#check if first 2 are letters
def isletter(s):
         if s[:2].isalpha():
               return True


def check_num_position(string):
    for i in range(len(string)):
        if string[i].isdigit():
            if string[i] == '0':
                return False
            return string[i:].isdigit()
    return True

main()
