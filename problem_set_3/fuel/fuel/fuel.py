def get_fuel(fraction):
    x=int(fraction[0])  #assign the first num to x as the divident
    y=int(fraction[1])  #assign the second numto y as the divesor

    #check if x is greater than y
    if x>y:
        raise ValueError("Numerator cannot be greater than denominator")

    # check ensures both x and y are positive integers
    if x < 0 or y <= 0:
        raise ValueError("Numerator and denominator must be positive")

    #convert fraction to percentage
    percentage=round(((x/y)*100))

    if percentage<=1 :
        print ('E')
    elif percentage>=99:
       print ('F')
    else:
     print(f"{percentage}%")

def main():
    while True:
        try:
            fraction=(input('Fraction:' )).split("/")
            get_fuel(fraction)
            break
        except ZeroDivisionError:
            print('cannot divide by 0')
        except ValueError:
            print ('enter valid numeric values')

main()
