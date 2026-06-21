import sys
sys.path.insert(0, '/Users/mac/Desktop/ai110project1')

from logic_utils import check_guess, update_score, parse_guess, get_range_for_difficulty


class TestCheckGuess:
    """Test the check_guess function for correctness of hints."""
    
    def test_guess_too_high_gives_go_lower_hint(self):
        """BUG FIX #1: Verify 'Too High' now correctly says 'Go LOWER!'"""
        outcome, message = check_guess(60, 50)
        assert outcome == "Too High"
        assert "Go LOWER!" in message, f"Expected 'Go LOWER!' but got '{message}'"
    
    def test_guess_too_low_gives_go_higher_hint(self):
        """Test 'Too Low' correctly says 'Go HIGHER!'"""
        outcome, message = check_guess(30, 50)
        assert outcome == "Too Low"
        assert "Go HIGHER!" in message, f"Expected 'Go HIGHER!' but got '{message}'"
    
    def test_guess_correct(self):
        """Test winning guess."""
        outcome, message = check_guess(50, 50)
        assert outcome == "Win"
        assert "Correct" in message


class TestUpdateScore:
    """Test the update_score function for correct penalizing."""
    
    def test_too_high_always_deducts_points(self):
        """BUG FIX #2: Verify 'Too High' always decreases score by 5."""
        # Even attempt (was buggy before)
        score = update_score(100, "Too High", 2)
        assert score == 95, f"Expected 95 but got {score} (was awarding +5 before fix)"
        
        # Odd attempt
        score = update_score(100, "Too High", 3)
        assert score == 95, f"Expected 95 but got {score}"
    
    def test_too_low_always_deducts_points(self):
        """Test 'Too Low' consistently decreases score by 5."""
        score = update_score(100, "Too Low", 1)
        assert score == 95, f"Expected 95 but got {score}"
        
        score = update_score(100, "Too Low", 2)
        assert score == 95, f"Expected 95 but got {score}"
    
    def test_scoring_is_symmetric(self):
        """Verify both 'Too High' and 'Too Low' have same penalty."""
        score_high = update_score(100, "Too High", 5)
        score_low = update_score(100, "Too Low", 5)
        assert score_high == score_low, "Scoring penalty should be same for Too High and Too Low"
    
    def test_win_gives_bonus_points(self):
        """Test winning gives points based on attempts."""
        # Win on attempt 1: 100 - 10*(1+1) = 80
        score = update_score(0, "Win", 1)
        assert score == 80, f"Expected 80 for win on attempt 1, got {score}"


class TestParseGuess:
    """Test input parsing."""
    
    def test_valid_integer(self):
        """Test parsing valid integer."""
        ok, value, err = parse_guess("50")
        assert ok is True
        assert value == 50
        assert err is None
    
    def test_invalid_input(self):
        """Test parsing invalid input."""
        ok, value, err = parse_guess("abc")
        assert ok is False
        assert value is None
        assert err is not None


class TestDifficultyRanges:
    """Test difficulty ranges."""
    
    def test_easy_range(self):
        low, high = get_range_for_difficulty("Easy")
        assert (low, high) == (1, 20)
    
    def test_normal_range(self):
        low, high = get_range_for_difficulty("Normal")
        assert (low, high) == (1, 100)
    
    def test_hard_range(self):
        low, high = get_range_for_difficulty("Hard")
        assert (low, high) == (1, 50)
