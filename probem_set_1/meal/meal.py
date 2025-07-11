#prompt user for time
#if  time is >= 7 and time <8 then breakfast
#if  time is >= 12 and time <13 then luch
#if  time is >= 18 and time <19 then dinner
#else return nothing

def convert(time):
    hour,minute=time.strip().split(":")
    hour=float(hour)
    minute=float(minute)
    time=hour+minute/60
    return(time)

def main():
    time=input("What time is it?" )
    time=convert(time)
    if time >=7 and time<=8:
        print("breakfast time")
    elif time >=12  and time <=13:
        print("lunch time")
    elif time >=18 and time <=19:
        print("dinner time")


if __name__ == "__main__":
    main()
