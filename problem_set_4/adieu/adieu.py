import inflect


names=[]
p=inflect.engine()

try:

   while True:
        name=input()
        names.append(name)

except EOFError:
    print(f"Adieu, adieu, to {p.join(names)}")


#MANUAL IMPLEMENTATION
"""
names = []

try:
    while True:
        name = input()
        names.append(name)
except EOFError:
    pass

#case where names is 1
if len(names) == 1:
    print(f"Adieu, adieu, to {names[0]}")

#case where names are 2
elif len(names) == 2:
    print(f"Adieu, adieu, to {names[0]} and {names[1]}")

#case where names are more than2
else:
    print("Adieu, adieu, to ", end="")
    second_last=len(names) - 2     #second last name

    for i in range(len(names)):
        if i <second_last :
            print(f"{names[i]}, ", end="")

        elif i == second_last:
            print(f"{names[i]}, and ", end="")
        else:
            print(names[i])
"""
