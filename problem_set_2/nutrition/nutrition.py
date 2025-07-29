"""
ask user to enter fuirt then should output the calories of a portion of that fruit according to the fda poster whichis available as text(fcreate function to read text)
ignore any input that is not a fruit
"""
#creact dictionary of fruit and calories
fruits={"Apple":130,"Avocado":50,"Banana":110,"Cantaloupe":50,"Grapefruit":60,
         "Grapes":90,"Honeydew Melon":50,"Kiwifruit":90, "Lemon":15,"Lime":20,
         "Nectarine":60,"Orange":80,"Peach":60,"Pear":100,"Pineapple":50,
         "Plums":70,"Strawberries":50,"Sweet Cherries":100,"Tangerine":50,"Watermelon":80,
        }

def getCalories(fruit):
        if fruit in fruits:
            print("Calories:",fruits.get(fruit))

def main():
    fruit=input("Item:" ).title()
    getCalories(fruit)

main()
