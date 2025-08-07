def main():
    while True:
        try:
            fraction=(input('Fraction:' ))
            fraction=convert(fraction)
            print(gauge(fraction))
            break
        except ZeroDivisionError:
            print('cannot divide by 0')
        except ValueError:
            print ('enter valid numeric values')

#convert fraction to percentage
def convert(fraction):
    fraction=fraction.split("/")
    x=int(fraction[0])  #assign the first num to x as the divident
    y=int(fraction[1])  #assign the second numto y as the divesor

    if y==0:
        raise ZeroDivisionError("cannot divide by 0")

    #check if x is greater than y
    if x>y:
        raise ValueError("Numerator cannot be greater than denominator")

    # check ensures both x and y are positive integers
    if x < 0 or y <= 0:
        raise ValueError("Numerator and denominator must be positive")

    percentage=round(((x/y)*100))
    return percentage


def gauge(percentage):
    if percentage<=1 :
            return 'E'
    elif percentage>=99:
       return 'F'
    else:
        return f"{percentage}%"



if __name__ == "__main__":
    main()




