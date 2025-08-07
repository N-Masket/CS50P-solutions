def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Rule 1: length must be between 2 and 6 inclusive
    if not (2 <= len(s) <= 6):
        return False

    # Rule 2: must start with at least two letters
    if not s[:2].isalpha():
        return False

    # Rule 3: all characters must be alphanumeric
    if not s.isalnum():
        return False

    # Rule 4: numbers, if any, must come at the end
    for i, char in enumerate(s):
        if char.isdigit():
            if char == "0":
                return False  # first number can't be 0
            return s[i:].isdigit()
    return True  # No numbers, or numbers are at end

if __name__ == "__main__":
    main()
