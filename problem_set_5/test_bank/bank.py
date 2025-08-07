def main():
    greeting=input("Greating: ")
    print(value(greeting))

def value(greeting):
    greeting=greeting.lower().strip()
    
    if greeting.startswith("h") and "hello" not in greeting:
       return 20

    elif "hello" in greeting:
       return 0

    else:
        return 100


if __name__=="__main__":
    main()
