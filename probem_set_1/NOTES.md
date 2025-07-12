## 1. Deep Thought

**Goal**:  
Respond to the question "What is the Answer to the Great Question of Life, the Universe, and Everything?" regardless of case or phrasing variations.

**Key Concepts**:  
- Case-insensitive comparison  
- `.lower()` and `.strip()` for input normalization  
- `match-case` with multiple pattern options

**Approach**:  
I used `.lower()` and `.strip()` on the input to normalize the string, making the comparison flexible to casing and spacing. Then I used `match-case` with multiple options (`"42"`, `"forty-two"`, `"forty two"`) in a single case line, it made the logic clean and easy to read.

**What I Learned**:  
- How `match-case` works nicely with multiple string options.  
- Why it's useful to clean input early before comparing it.  
- That simple logic can still benefit from using newer Python syntax for readability.

## 2. Home Federal Savings Bank

**Goal**:  
Respond with different outputs depending on how a user greets you:  
- If the greeting starts with “hello”, respond with `$0`  
- If it starts with “h” but not “hello”, respond with `$20`  
- Otherwise, respond with `$100`

**Key Concepts**:  
- String normalization with `.lower()` and `.strip()`  
- `startswith()`  
- Logical condition ordering

**Approach**:  
I normalized the input using `.lower().strip()`. To determine the correct response, I checked if the greeting started with `"h"` but wasn't `"hello"`, using `startswith("h") and "hello" not in greeting`.  
Then, I separately checked for `"hello"` as a substring.  
Eventually I realized that **checking for `"hello"` first** avoids accidentally classifying `"hello"` under the `"h"` condition  so the **order of conditions matters** more than I expected.

**What I Learned**:  
- Condition order can change your program's logic in subtle ways.  
- Using both `in` and `startswith()` helps write flexible comparisons.  
- Input normalization is key to handling messy or inconsistent input.

## 3. File Extensions

**Goal**:  
Prompt the user for a file name and return the corresponding media type based on its extension.

**Key Concepts**:  
- String methods: `.lower()`, `.strip()`, and `.endswith()`  
- Chained `elif` statements for checking multiple conditions  
- Default case using `else`

**Approach**:  
I cleaned up the user input by converting it to lowercase and removing leading/trailing spaces. Then I used `.endswith()` to check for known file types (like `.gif`, `.jpg`, `.pdf`, etc.). If no known type matched, I returned `"application/octet-stream"` as the default.

**What I Learned**:  
- `.endswith()` is perfect for file extension checks.  
- Chaining conditions keeps the logic readable and manageable.  
- Always include a fallback (`else`) when handling unknown input.

## 4. Math Interpreter

**Goal**:  
Take a simple arithmetic expression like `"3 + 4"` and compute the result.

**Key Concepts**:  
- Input parsing and splitting  
- Type casting with `float()`  
- Arithmetic operations  
- Defensive programming (e.g., divide-by-zero check)

**Approach**:  
I used `.split()` to separate the expression into operands and operator, then converted the numbers to floats. My `calculate()` function used `if/elif` to perform the correct operation. I also included a check for division by zero.

**What I Learned**:  
- How to break a string into usable components.  
- Structuring logic with separate functions improves clarity.  
- Why it's important to anticipate runtime errors like division by zero.  
- How to format output with one decimal place using `:.1f`

## 5. Meal Time

**Goal**:  
Ask the user for the current time in `HH:MM` format and determine if it’s breakfast, lunch, or dinner time.

**Key Concepts**:  
- Splitting strings with `:`  
- Converting time into decimal format (`hour + minute / 60`)  
- Conditional ranges using floats

**Approach**:  
I split the user’s time input into `hour` and `minute`, converted them to floats, and calculated a single decimal value for easier comparison. Then I checked if the time fell into the specified meal time ranges.

**What I Learned**:  
- That representing time as a single float makes range comparisons simpler.  
- How to use basic math to convert time formats.  
- The importance of clean input parsing for real-world formats like time.


