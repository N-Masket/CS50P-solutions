grocery=[]
while True:
    try:
        item=input().upper()
        grocery.append(item)

    except EOFError:
        #loop goes through each unique item in the list only once.
        for item in sorted(set(grocery)) :
            quantity=grocery.count(item)
            print(quantity,item,)

        break
