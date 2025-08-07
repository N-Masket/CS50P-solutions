#promt user to enter expression
def main():
    expression=(input("Expression: "))
    x,y,z=expression.strip().split()
    x=float(x)
    z=float(z)
    answer=calculate(x,y,z)


def calculate(x, y, z):
    if y == "+":
        print(f"{x + z:.1f}")
    elif y == "-":
        print(x - z)
    elif y == "*":
        print(x * z)
    elif y == "/":
        if z != 0:
           print(f"{x / z:.1f}")
        else:
            print("Cannot divide by zero")
    else:
       print("Invalid operator")


main()
