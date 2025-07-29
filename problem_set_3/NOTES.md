## 1. Fuel Gauge

**Goal**:  
Prompt the user to input a fuel fraction (e.g., `3/4`), convert it to a percentage, and return:
- `"E"` if it's ≤ 1%
- `"F"` if it's ≥ 99%
- The percentage (e.g., `"75%"`) otherwise

**Key Concepts**:  
- String splitting  
- Type casting and division  
- Value validation (zero denominator, invalid format)  
- Error handling with `try`/`except` and `while True` loop

**Approach**:  
I split the input on the `/` to separate numerator and denominator, then converted them to integers. To prevent crashes, I wrapped everything in a `try/except` block and used a `while True` loop to re-prompt the user until valid input was given.

I rounded the result to the nearest whole number, and used conditionals to return `"E"`, `"F"`, or the actual percentage.

**What I Learned**:  
- How to build programs that handle invalid input gracefully.  
- The power of `while True` when combined with `try/except` for input loops.  
- Rounding numbers properly and using clean logic to map values to custom output.  
- Validating fractions and understanding how different inputs could crash the code if not handled carefully.


## 2. Taqueria

**Goal**:  
Prompt the user to order items from a menu and return the running total cost of all valid items ordered. Stop when the user signals EOF (Ctrl+D or Ctrl+Z).

**Key Concepts**:  
- Dictionaries for menu storage  
- Looping with `while True`  
- `try/except` for handling EOFError  
- Case-insensitive matching and `.title()` for formatting

**Approach**:  
I created a dictionary to store menu items and their prices. I used a `while True` loop to keep prompting the user for input until an EOFError was raised. I used `.title()` to match the input to the dictionary keys since the input might be lowercase.

Each valid menu item added to the total cost. If the user entered something not on the menu, the input was ignored without crashing the program.

**Challenges Faced**:  
- Handling `EOFError` was new territory ,figuring out how to gracefully exit the loop without using `break` took a bit of experimenting.  
- Matching user input to dictionary keys was tricky because capitalization mattered, so I had to normalize the input correctly using `.title()` or `.casefold()`.  
- It was hard at first to decide whether to print inside the loop or collect and print at the end .Eventually, I printed the total after each valid entry.

**What I Learned**:  
- How to work with dictionaries to simulate real-world systems like a menu.  
- That user input often needs cleaning to match program expectations.  
- How `try/except` can be used not just for errors but to *end* a loop gracefully.  
- Coding something that "feels real" is incredibly rewarding, it reminded me of how code interacts with people in everyday contexts.

## 3. Grocery

**Goal**:  
Let the user enter grocery items one at a time. Count how many of each item were entered, and print a sorted list with the quantity of each item.

**Key Concepts**:  
- Lists for item collection  
- Sets for uniqueness  
- `list.count()` to calculate frequency  
- Input normalization using `.upper()`  
- `try/except` to handle EOF

**Approach**:  
I stored all items in a list after normalizing them to uppercase. To avoid printing duplicate items, I converted the list to a **set** , which automatically ensures uniqueness  and sorted it alphabetically.

Then, for each unique item, I used `.count()` to tally how many times it appeared in the original list and printed the result.

**Challenges Faced**:  
- My initial challenge was figuring out how to *track frequency* without printing duplicates.  
- I originally thought a dictionary would be necessary, but using a `set()` for uniqueness and `.count()` for frequency gave me a cleaner, simpler solution.  
- Working through this reminded me that **understanding data structures gives you flexibility** — once you know your tools, you can improvise!

**What I Learned**:  
- A `set` is perfect for filtering duplicates while a `list` is great for storing order and frequency.  
- You don’t always need a dictionary to solve a frequency problem ,sometimes a creative combination of structures does the trick.  
- Don’t be afraid to trust your approach, especially when testing different ways to solve the same problem.  
- Python gives you multiple paths, the best one is the one you understand and can explain.


## 4. Outdated

**Goal**:  
Prompt the user for a date in either `"September 8, 1636"` or `"9/8/1636"` format, validate it, and return the date in `YYYY-MM-DD` format.

**Key Concepts**:  
- String parsing and format validation  
- Handling multiple input patterns  
- List indexing and cleanup with `.split()`  
- Input normalization using `.strip()` and `.title()`  
- `try/except` for safely handling user errors

**Approach**:  
I used `split()` to break down the input and checked whether it followed the slash or comma format. I also normalized the month names with `.title()` and used a list of month names to convert them into numbers.

I wrapped the whole logic in a `try/except` to handle anything unexpected, like invalid dates or wrong formats.

**Challenges Faced**:  
- Honestly, this was the **toughest problem so far**. Validating two very different input formats was mentally draining.  
- Parsing the month name correctly and converting it into a number took multiple failed attempts.  
- I realized my code was getting messy, which made debugging harder and that’s when it clicked: **I needed to separate logic into smaller, testable parts.**  
- This challenge forced me to slow down, plan the logic more clearly, and write modular code.  

**What I Learned**:  
- Input validation is *everything* when you’re working with user data.  
- Modularity = clarity. Breaking the logic into functions makes the code more readable and easier to fix/test.  
- You don’t need to solve everything in one line ; clarity beats cleverness.  
- It’s okay to struggle ,these moments are where real growth happens.


## 🧠 Final Reflections – Problem Set 3

This set really stretched me , not just technically, but mentally. From seemingly simple problems like *Fuel Gauge* to surprisingly tricky ones like *Outdated*, I found myself bumping into logic walls that forced me to rethink how I write, test, and structure code. 

The biggest shift for me was realizing that modular code isn’t just about writing “neat” programs, it’s about **surviving complexity**. By breaking things down, I started seeing how each part of the problem fit together, and how smaller units could be tested or fixed independently.

I also rediscovered how powerful Python’s data structures are . Whether I was using a `set` to solve *Grocery* in my own way, or handling user input edge cases with `try/except`. This problem set taught me that knowing your tools gives you room to be creative.

Most importantly, I’m learning to keep going  even when I hit a wall. Problem solving isn’t always about having the answer; sometimes, it’s about staying with the question long enough to grow into it.
