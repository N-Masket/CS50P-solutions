# Notes – Problem Set 0

## 1. Indoor Voice
**Goal**: Take user input and convert it to lowercase.
**Key concept**: `.lower()` method and string input handling.

**What I learned**:
- How to work with string methods.
- The difference between `return` and `print()` in a function and how it affects the result when the function is called (something I overlooked but very important when aiming for a certain output).
- Simplicity is powerful!

---

## 2. Playback Speed
**Goal**: Replace spaces in user input with `...` to simulate a playback effect.
**Key concept**: Initially explored `sep`, then `.join()`, and finally settled on `.replace()`.
**Approach**:
At first, I tried using the `sep` method so that at each point of separation, the program would insert the three dots — but that didn't work. I proceeded to use the `.join()` method, although now that I think about it, the `replace()` method would make more sense since this is string-based, not a data structure problem.

**What I learned**:
- Replacing characters in strings with ease.
- It’s okay to try multiple approaches and then refine your solution.

---

## 3. Making Faces
**Goal**: Replace every occurrence of an emoticon with its emoji equivalent.
**Approach**:
I used the `.replace()` method I discovered in the previous challenge.

**What I learned**:
- Reusing methods across problems makes you more confident with them.

---

## 4. Einstein
**Goal**: Find the number of joules using Einstein’s equation.
**Key concept**: Using `input()` and applying the formula \( E = mc^2 \).

**What I learned**:
- There are multiple ways to find the power of a number.
- I challenged myself to explore alternatives to the `math` library and discovered that Python’s `**` operator can be just as useful.

---

## 5. Tip Calculator
**Goal**: Calculate the tip based on bill and percentage.
**Approach**:
I used `.replace()` to remove the currency and percentage symbols.

**What I learned**:
- Solving a problem is easier when you have an idea of what tools to use.
- Read as much as you can and practice — it helps develop “muscle memory” and builds confidence to solve problems more efficiently.
