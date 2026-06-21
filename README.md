# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Game Purpose:** This is an educational debugging exercise where students play a Streamlit-based number guessing game that contains intentional bugs. The game challenges players to guess a random secret number within a difficulty-dependent range (Easy: 1-20, Normal: 1-100, Hard: 1-50) with a limited number of attempts. Each correct direction guess reduces the score, and reaching the correct number earns bonus points based on how quickly they guessed.

**Bugs Found:**
1. **Reversed Hint Directions** — When a guess was too high, the game said "Go HIGHER!" instead of "Go LOWER!" This completely reversed the feedback mechanic and made the game unplayable.
2. **Asymmetric Scoring** — Wrong guesses on even-numbered attempts would award +5 points instead of deducting -5 points, making the scoring system inconsistent and unpredictable.
3. **String Type Conversion on Even Attempts** — The secret number was intentionally converted to a string on even attempts, causing lexicographic string comparisons (e.g., "9" > "10" is True) that broke the high/low logic.

**Fixes Applied:**
1. Extracted all game logic into `logic_utils.py` for better separation of concerns
2. Corrected hint directions in `check_guess()` to match actual comparison results
3. Removed the asymmetric scoring penalty in `update_score()` to consistently deduct 5 points for all wrong guesses
4. Created comprehensive pytest suite with 12 tests to verify all fixes work correctly

## 📸 Demo Walkthrough

This walkthrough demonstrates how the fixed game now works correctly:

1. **Start the Game** — Run `python -m streamlit run app.py` and select "Normal" difficulty in the sidebar. The game displays "Guess a number between 1 and 100" with 8 attempts allowed.

2. **First Guess** — User enters a guess of 40. The Developer Debug Info shows the secret is 75. Since 40 < 75, the game returns "Too Low" with hint "📈 Go HIGHER!" which is now correct.

3. **Second Guess** — User enters 70. Since 70 < 75, the game returns "Too Low" with hint "📈 Go HIGHER!" Score decreases by 5 (from 0 to -5).

4. **Third Guess** — User enters 80. Since 80 > 75, the game returns "Too High" with hint "📉 Go LOWER!" which is now correct (was previously showing "Go HIGHER!"). Score decreases by 5 again.

5. **Winning Guess** — User enters 75. The game displays "🎉 Correct!" with celebration balloons and shows "You won! The secret was 75. Final score: 65" (100 - 10*3 - 5 - 5 = 65 points).

**Key Fixes Demonstrated:**
- Hints now correctly indicate direction (was reversed before)
- Score consistently decreases for wrong guesses, regardless of attempt number (was asymmetric)
- All game mechanics work smoothly across multiple attempts

## 🧪 Test Results

```
$ pytest test/test_game_logic.py -v

test/test_game_logic.py::TestCheckGuess::test_guess_too_high_gives_go_lower_hint PASSED [  8%]
test/test_game_logic.py::TestCheckGuess::test_guess_too_low_gives_go_higher_hint PASSED [ 16%]
test/test_game_logic.py::TestCheckGuess::test_guess_correct PASSED       [ 25%]
test/test_game_logic.py::TestUpdateScore::test_too_high_always_deducts_points PASSED [ 33%]
test/test_game_logic.py::TestUpdateScore::test_too_low_always_deducts_points PASSED [ 41%]
test/test_game_logic.py::TestUpdateScore::test_scoring_is_symmetric PASSED [ 50%]
test/test_game_logic.py::TestUpdateScore::test_win_gives_bonus_points PASSED [ 58%]
test/test_game_logic.py::TestParseGuess::test_valid_integer PASSED       [ 66%]
test/test_game_logic.py::TestParseGuess::test_invalid_input PASSED       [ 75%]
test/test_game_logic.py::TestDifficultyRanges::test_easy_range PASSED     [ 83%]
test/test_game_logic.py::TestDifficultyRanges::test_normal_range PASSED   [ 91%]
test/test_game_logic.py::TestDifficultyRanges::test_hard_range PASSED     [100%]

========================= 12 passed in 0.01s =========================
```

✅ **All 12 tests passing!** The fixed game correctly handles hint directions, symmetric scoring, input parsing, and difficulty ranges.

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
