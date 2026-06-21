# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game, I immediately noticed several critical issues with the game logic. The hints were completely reversed — when I guessed a number too high, the game told me to "Go HIGHER!" instead of "Go LOWER!" This made it impossible to follow the feedback. On top of that, I noticed the scoring system was broken: sometimes a wrong guess would add points to my score instead of deducting them. The game also had trouble in restarting the game.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 80 when secret is 50 | Display "Too High" with hint "Go LOWER!" | Display "Too High" with hint "Go HIGHER!" | none |
| Guess 9 on attempt 2 when secret is 10 | Display "Too Low" (9 < 10) | Display "Too High" (treats as string: "9" > "10") | none |
| Guess too high on attempt 2 (even number) | Deduct 5 points from score | Add 5 points to score | none |
| | | | |

---

## 2. How did you use AI as a teammate?

I used Claude Code (Claude AI agent) to help debug and refactor this project. The AI correctly identified the root causes of all the bugs by analyzing the code statically, which was much faster than manually tracing through the logic myself.

**Example of Correct AI Help:** The AI suggested extracting all game logic functions into a separate `logic_utils.py` file to keep concerns separated. I followed this refactoring approach, and it made the code cleaner and the bugs easier to fix in one focused location. I verified this was correct by confirming the app still runs properly after the refactor.

**Example of Misleading AI Help:** Early on, the AI suggested I might need to manually run the game multiple times with different inputs to observe all bugs. This seemed impractical for quick debugging. Instead, I asked the AI to analyze the code directly and point out logical errors — a much more efficient approach. The lesson was to leverage the AI's code-reading ability rather than relying solely on manual testing.

---

## 3. Debugging and testing your fixes

I used pytest to verify each fix worked correctly. For the reversed hints bug, I created a test that checked whether `check_guess(60, 50)` returned a message containing "Go LOWER!" — it now does. For the scoring bug, I tested `update_score(100, "Too High", 2)` on an even attempt and verified it now correctly decreases the score to 95 instead of increasing it to 105.

I ran a full test suite with 12 automated tests that all passed, including tests for win scoring, input parsing, and difficulty ranges. These tests gave me confidence that the fixes worked correctly without breaking other functionality.

The AI helped me structure the test file by suggesting clear test class organization (one class per function) and meaningful test names. It also suggested testing both odd and even attempts separately to catch the asymmetric scoring bug completely.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
