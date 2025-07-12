# Notes – Problem Set 2

## 1. camelCase

**Goal**:  
Convert a variable name from `camelCase` to `snake_case`.

**Key Concepts**:  
- Looping through characters (`for` loop)  
- Using conditionals (`if` and `while`)  
- String methods like `.islower()` and `.isupper()`  
- List manipulation and `.join()`

**Approach**:  
I used a `for` loop to iterate over each character in the input string. Inside the loop, I experimented with a `while` loop to check if a character is lowercase, appending it directly. The `while` loop here only runs once because I immediately `break` it ,effectively acting like an `if` statement.For uppercase letters, I converted them to lowercase and added an underscore before them to build the `snake_case` version.
I realize that an `if` statement would have been more straightforward since the condition only needs checking once before deciding the flow but since I wanted to improve my comfort with `while` loops (especially after struggling with them in the Coke Machine problem), I tested this approach on purpose.

**What I Learned**:  
- Sometimes `if` statements are better suited for single-condition checks inside loops.  
- Using `while` with an immediate `break` works but can be less clear,clarity matters!  
- Practicing different ways to solve a problem helps deepen understanding, even if some ways aren’t the most efficient.  
- The process of iterating, checking cases, and building new strings is a great exercise in string manipulation fundamentals.


## 2. Coke Machine

**Goal**:  
Simulate a coke vending machine where a user inserts coins until reaching 50 cents. If the user overpays, the machine returns change.

**Key Concepts**:  
- `while` loops  
- Conditional checks (`if`, `elif`)  
- Input validation  
- Arithmetic operations

**Approach**:  
I used a `while` loop that keeps asking the user to insert coins until the total reaches or exceeds 50 cents. I added conditions to only accept specific coin values (5, 10, or 25). If the total exceeds 50, I calculated and returned the correct change.

**What I Learned**:  
- How to create a loop that tracks cumulative input from the user  
- The importance of validating input (accepting only allowed coin values)  
- How to manage logic for exact payment vs overpayment (and return correct change)
- Using clean and clear conditions keeps the logic easier to debug and build on

**Take-Aways**:  
- This activity highlighted how `while` loops aren't my strongest suit as I definitely underestimated them at first.
- The more I worked through the logic, the more it started to click. It reminded me that sometimes you only truly understand a concept when you wrestle with it hands-on.
- I still want to dive deeper into understanding the difference between `while-else` and `while`.
- Overall, it’s a good reminder that loops are powerful but only if you learn how to control their flow properly.

## 3. Just setting up my twttr

**Goal**:  
Remove all vowels from a user’s input and return the result as a string.

**Key Concepts**:  
- Lists and strings  
- Looping through characters  
- List comprehension  
- Membership testing (`in`)

**Approach**:  
At first, I thought of creating two lists ; one for vowels and another to hold characters that aren’t vowels. I considered using the `remove()` method but realized that it doesn’t work on strings (a learning moment for me). Eventually, I discovered list comprehension, which was fast and elegant but honestly, I didn’t fully get it right away.I had to break it down step by step to understand it. That process reminded me that **faster or more advanced methods are only helpful if you understand them**. It's okay to start with what you know and grow from there, no need to rush mastery.

**What I Learned**:  
- List comprehensions are powerful, but I need to be comfortable with the basics first.  
- There's value in **exploring ideas**, even if they don’t work as they often lead you to unexpected learning.  
- Sometimes the idea you try will fail, but it'll push you to understand the language deeper.  
- I’m learning not to skip the process: read the problem → picture it → jot down all possible approaches → test them → combine or discard as needed.  
- Coding is becoming less about just solving, and more about experimenting and learning *why* something does or doesn’t work.

## 4. Vanity Plates

**Goal**:  
Validate a vanity plate based on several rules:
- It must start with at least two letters.
- It must be 2–6 characters long.
- Numbers (if any) must appear at the end.
- The first number used must not be 0.
- No periods, spaces, or punctuation allowed.

**Key Concepts**:  
- Conditional logic with multiple layers  
- String slicing  
- `isalpha()`, `isdigit()`, and `.isalnum()`  
- Error-checking in stages  
- Rearranging logic for better flow

**Approach**:  
This one was tough. I understood the individual rules and knew which Python methods to use (`isalpha`, `isdigit`, etc.), but bringing them together in a way that passed all `check50` tests took time.The rule about **"the first number must not be 0"** tripped me up the most. I had ideas for how to find the first digit, but figuring out how to isolate and evaluate it took several rearrangements of my code.
Eventually, I got better results by testing each rule one at a time and organizing my logic in stages. I’m glad I didn’t give up ; I kept reworking my code until it made sense and behaved correctly.

**What I Learned**:  
- Complex validation is easier when you break it into clear, testable chunks.  
- Don't rush, sometimes writing a “wrong” solution helps you figure out the right one.  
- Rearranging your code helps you see how flow affects output (and `check50` results).  
- Persistence pays off and it's okay to struggle if you're learning something in the process.
`.isalnum()` was new to me :it checks whether a string is made up only of letters and numbers, and it helped with filtering out invalid characters.Super useful when you dont want to deal with regex  

## 5. Nutrition Facts

**Goal**:  
Prompt the user for a fruit and return its calorie content, based on a predefined list.

**Key Concepts**:  
- Dictionaries (`dict`)  
- Case-insensitive comparison  
- Input handling and normalization  
- Key lookups using `.get()` or `in`

**Approach**:  
I created a dictionary that stores fruit names as keys and their calorie values as values. Then I took the user's input, converted it to ``title()`to ensure case-insensitive comparison, and checked if the input was a valid fruit in the dictionary.If the fruit existed, I displayed the corresponding calorie value; otherwise, I did nothing (as per the spec). This felt pretty straightforward, but it also helped reinforce how useful dictionaries are when it comes to storing and looking up structured data quickly.

**What I Learned**:  
- How dictionaries can be used for quick key-based lookups.  
- The importance of **normalizing input** (like using `.title()`) to handle variation in user input.  
- How to avoid errors by checking if a key exists before accessing it.  
- Even when a problem seems “simple,” thinking about edge cases (like capitalized input or typos) is a good habit to build early.


---

## 🧠 Final Reflections – Problem Set 2

Problem Set 2 really stretched my ability to think logically and carefully structure my code. It wasn’t just about writing something that works, it was about writing code that works *correctly*, under all the rules and edge cases.I faced challenges, especially with loops, conditional layering, and validation logic. But each challenge helped me dig deeper into the language. I also learned the value of slowing down, organizing my thoughts, and exploring different approaches without rushing to the “most efficient” solution right away.

This set reminded me that real progress isn’t just getting everything right the first time, it’s pushing through confusion, adjusting your thinking, and learning to trust your growth.

On to Problem Set 3 🚀
