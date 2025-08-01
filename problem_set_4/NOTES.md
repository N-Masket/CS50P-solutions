## 1. Emojize

**Goal**:  
Convert text containing emoji aliases (like `:smile:`) into actual emojis using the `emoji` library.

**Key Concepts**:  
- Using third-party libraries (`emoji`)  
- Understanding function usage (`emojize`)  
- Simple string transformation

**Approach**:  
This challenge felt straightforward. I used the `emoji.emojize()` function to convert input strings with emoji aliases to their emoji counterparts. It was surprisingly easy ; no tricks, just a neat library doing the work.

**What I Learned**:  
- How to use external Python libraries to simplify tasks.  
- Sometimes, the simplest solutions are the best no need to overcomplicate.  
- Exploring new libraries can be fun and immediately useful.


## 2. Figlet

**Goal**:  
Create a program that accepts command-line arguments to set a font style and prints user input as stylized ASCII art using `pyfiglet`.

**Key Concepts**:  
- Command-line argument parsing (`sys.argv`)  
- Working with third-party libraries (`pyfiglet`)  
- Handling errors and invalid font input  
- Conditional logic placement

**Approach**:  
Understanding how `sys.argv` works was crucial for this challenge. Once I understood how to read command-line arguments and differentiate between valid and invalid cases (like too many or unsupported fonts), the rest came together cleanly.

I used `if` conditions to check for how many arguments were passed, then validated the font name using `FigletFont.getFonts()` before rendering the final text.

**Challenges Faced**:  
- My **conditional placement** mattered a lot;the order in which I validated inputs affected the entire flow.  
- At first, I overlooked checking for invalid fonts and the program would crash .That reminded me to build defensively.  
- I had to look up how to properly list available fonts and compare them against user input.

**What I Learned**:  
- How to use `sys.argv` to accept and process command-line inputs.  
- That proper **order and structure of conditions** determines how well your program handles user errors.  
- Reinforced my confidence in using libraries like `pyfiglet` and combining them with logic I write myself.  
- Not all problems are complex but understanding the environment (like the command line) is key to solving them.

## 3. Adieu, Adieu

**Goal**:  
Prompt the user to input names and output them as a natural-language list with proper punctuation and the word "and" before the final name.

**Key Concepts**:  
- Lists and loops  
- Exception handling (`EOFError`)  
- String formatting logic  
- Optional: using the `inflect` module for human-friendly string formatting

**Approach**: 
I collected names using a `while True` loop and ended the input with `EOFError`. Then I used the `inflect.engine().join()` method to format the final list properly  with commas and the final “and” before the last name. It worked smoothly thanks to the `inflect` module.

While the problem suggested using the `inflect` module, I decided to challenge myself by doing it manually as well just to see how I’d handle formatting a human-readable list on my own. It worked… but barely at first!

Manually formatting the names exposed edge cases I hadn’t considered, like when the list only had two names (e.g., `Liesel and Friedrich`). That case kept failing for me, and I couldn’t understand why  until I realized it was **just punctuation** tripping me up.

**Challenges Faced**:  
- Handling special cases for different list lengths (1, 2, 3+)  
- Forgetting about commas and spacing  the little things that make or break the output  
- Being reminded that **“it works”** isn’t enough , **“it works as intended for all cases”** is the real win

**What I Learned**:  
- Having the *right* tools changes everything. The more I explore third-party libraries, the more confident I feel about solving real problems.  
- This task reminded me that reading documentation is not a chore — it’s a shortcut to powerful solutions.  
- Even simple problems can be opportunities to grow smarter about how I code and what resources I lean on.
- Doing things “the long way” can teach you way more than just using shortcuts.  
- Sometimes we get caught up trying to pass tests or make things work and overlook the little details that *really* matter.  
- If I had used `inflect` immediately, I wouldn’t have learned the complexity behind what it’s solving for us.  
- Humility check: even “small” punctuation matters in code  don’t overlook anything.

## 4. Guessing Game

**Goal**:  
Create a game where the computer picks a random number between 1 and a user-defined level, and the user must guess the number.

**Key Concepts**:  
- Random number generation (`random.randint()`)  
- Input validation with `try/except`  
- Looping until a correct guess is made  
- Conditional feedback (`Too large`, `Too small`, `Just right!`)

**Approach**:  
I first prompted the user to enter a difficulty level and used `random.randint()` to generate the target number. Then I entered a loop where the user could keep guessing until they got it right. For each guess, I used `try/except` to catch invalid inputs like letters or out-of-range numbers.

I provided feedback after each guess, helping the user adjust their answer until they guessed correctly.

**Challenges Faced**:  
- At first, I was unsure about when and where to place the `try/except` blocks, but I’ve really started to **understand how they control flow** and prevent crashes.  
- Ensuring the user only entered **positive integers** was something I had to think about deliberately.

**What I Learned**:  
- My understanding of `try/except` has grown asI now know how to use it to make my programs more resilient and user-friendly.  
- Games are a fun way to learn feedback loops and conditionals!  
- I’m learning to build interactive programs that keep running until a certain condition is met  and I’m loving how that feels in code.

## 5. Professor

**Goal**:  
Simulate a simple math quiz that asks the user random integer questions, gives them up to 3 attempts per question, and tracks their final score.

**Key Concepts**:  
- Random number generation  
- Looping with `while` and nested logic  
- Tracking score and attempts  
- Function design and modular thinking

**Approach**:  
This challenge *looked* simple on the surface, but had a lot going on beneath. At first, I was overwhelmed trying to figure out how to make everything work at once , generating random numbers, tracking attempts, scoring, etc.  

Then I paused and reminded myself:  
📌 *“Don’t solve the entire problem at once , solve it in pieces.”*

I started by getting random math questions to display, then moved on to input and response handling, then implemented the retry logic, and finally the scoring. Once I viewed it as a system with small components that needed to work together, everything became clearer.

**Challenges Faced**:  
- I was tempted to do too much at once.  
- Making sure each retry didn’t affect the overall flow was tricky at first.  
- It forced me to **fully understand the structure of the problem first**, then break it down.

**What I Learned**:  
- The power of modular thinking: breaking the problem into layers helped me build cleanly and avoid confusion.  
- That seeing the **full picture first** helps you map out the building blocks and their connections.  
- Writing code in stages and testing as you go is a huge time-saver.  
- You don’t have to know the full code at the beginning ,just understand the flow and work it section by section.

## 7. Bitcoin

**Goal**:  
Fetch and display the current price of Bitcoin in USD using the CoinCap API.

**Key Concepts**:  
- Making HTTP requests with the `requests` library  
- Parsing JSON responses  
- Handling API keys and headers  
- Formatting output

**Approach**:  
At first, I struggled with understanding how the API required specific headers to work properly. Once I figured out the exact structure for the request, including the API key and endpoint, fetching the data became straightforward. I parsed the JSON response to extract the Bitcoin price and formatted it for display.

**What I Learned**:  
- How to interact with a real-world API in Python.  
- The importance of reading API documentation carefully  headers and authentication matter!  
- Working with JSON data structures to extract meaningful info.

## 🌱 Final Reflections – Problem Set 4

This problem set felt like a pivot point in my CS50P journey :the moment things started to *click*. I wasn’t just writing code to pass tests anymore; I was **thinking like a developer**. From working with APIs and libraries like `pyfiglet`, `requests`, and `inflect`, to intentionally writing my own logic just to understand how things work behind the scenes ... I was growing.

I became more intentional with `try/except`, started paying attention to “small” things like punctuation, and realized that **reading documentation isn’t a weakness , it’s a superpower**. Each task, especially *Professor* and *Adieu*, pushed me to slow down, think structurally, and build things one layer at a time.

Most importantly, I’m learning to embrace my curiosity and trust the process. I’m no longer afraid to test ideas or rework my code  because every failed attempt teaches me something. Problem Set 4 was about leveling up, and I can honestly say: I did.
