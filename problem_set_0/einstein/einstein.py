#prompt user to enter mass
def joules():
    c=300000000
    mass=input('enter num of mass in kg:' )
    energy=int(mass)*(c**2)
    print(energy)

joules()
