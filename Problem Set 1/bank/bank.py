#promt user for a greating , remove whitespace and case insensitive
#if greeting equal hello output 0
#if greeting starts with h but not equal hello output 20
#else  greeting outputs 100

greeting=input("Greating: ").lower().strip()

if greeting.startswith("h") and "hello" not in greeting:
   print("$20")
elif "hello" in greeting:
    print("$0")
else:
    print("$100")
