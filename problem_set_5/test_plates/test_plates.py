from plates import is_valid

# Test length boundaries
def test_length():
    assert is_valid("A") == False          # Too short
    assert is_valid("ABCDEFG") == False    # Too long
    assert is_valid("CS50") == True        # Valid length
    assert is_valid("AB") == True          # Min valid length

# Test starting characters
def test_starts_with_letters():
    assert is_valid("50CS") == False       # Starts with numbers
    assert is_valid("A1") == False        # Only 1 letter

# Test number placement and zero rule
def test_number_position():
    assert is_valid("CS05") == False       # Leading zero in number
    assert is_valid("CS5O0") == False      # Letters after number

# Test disallowed characters
def test_non_alphanumeric():
    assert is_valid("CS!50") == False      # Punctuation
    assert is_valid("CS 50") == False      # Space
    assert is_valid("CS@50") == False      # Symbol

