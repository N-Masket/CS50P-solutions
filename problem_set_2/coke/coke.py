#method to validate amount and perform calculations
def checkAmount():
    total = 0

    while total < 50:   #loop runs until condiion(total less than 50) is true
        coin = int(input("Insert coin: "))

        if coin in [5, 10, 25]:    #checks if the coin inserted is an aceppted denomination
            total += coin          #tracks how much the user has inserted in total
            if total < 50:
                print("Amount Due:", 50 - total)    #subtracts the inserted amount (total) from the 50
        else:
            print("Amount Due:", 50 - total)  # Show updated amount due even after invalid

    # total is 50 or more (condition is false)
    if total > 50:
        print("Change Owed:", total - 50)
    else:
        print("Change Owed: 0")


def main():
    print("Amount Due: 50") #inform user how much  is due at beginning of program
    checkAmount()

main()



