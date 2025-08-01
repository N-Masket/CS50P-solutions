import pyfiglet
from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = pyfiglet.FigletFont.getFonts()
figlet.setFont(font=random.choice(fonts))

# No arguments
if len(sys.argv) == 1:
    print("Invalid usage")
    sys.exit()

# Exactly 2 arguments
elif len(sys.argv) == 3:

    if sys.argv[1] in ("-f", "--font"):   #check if f or--font in first arg

        if sys.argv[2] in fonts:    #check if argv[2] input is a valid font
            text = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(text))
        else:
            print("Invalid usage")
            sys.exit(1)
    else:
        print("Invalid usage")  # invalid flag
        sys.exit(1)

# Any other case
else:
    print("Invalid usage")
    sys.exit(1)

