#prompt user for input

answer=input("what is the answer to the Great Question of Life, the Universe, and Everything?" ).lower().strip()

#if answer is 42 or forty-two or forty two, return yes else no

match answer:
    case "42" |"forty-two"| "forty two":
        print("Yes")
    case _:
        print("No")

