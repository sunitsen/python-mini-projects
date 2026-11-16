"""Number guessing game: class variables, classmethod factory, staticmethod validation."""
import random


class GuessingGame:
    DIFFICULTIES = {"easy": (1, 10, 5), "medium": (1, 50, 7), "hard": (1, 100, 7)}

    def __init__(self, low, high, max_attempts):
        self.low = low
        self.high = high
        self.max_attempts = max_attempts
        self.attempts = 0
        self.secret = random.randint(low, high)

    @classmethod
    def from_difficulty(cls, name):
        """Alternative constructor."""
        if name not in cls.DIFFICULTIES:
            raise ValueError(f"Choose from: {', '.join(cls.DIFFICULTIES)}")
        return cls(*cls.DIFFICULTIES[name])

    @staticmethod
    def is_valid_guess(text, low, high):
        return text.isdigit() and low <= int(text) <= high

    def check(self, guess):
        """Returns 'low', 'high' or 'correct'."""
        self.attempts += 1
        if guess < self.secret:
            return "low"
        if guess > self.secret:
            return "high"
        return "correct"

    @property
    def attempts_left(self):
        return self.max_attempts - self.attempts

    def play(self):
        print(f"Guess the number between {self.low} and {self.high}. "
              f"You have {self.max_attempts} attempts.")
        while self.attempts_left > 0:
            text = input("Your guess: ").strip()
            if not self.is_valid_guess(text, self.low, self.high):
                print("Invalid guess, try again.")
                continue
            result = self.check(int(text))
            if result == "correct":
                print(f"You won in {self.attempts} attempts!")
                return True
            print(f"Too {result}! Attempts left: {self.attempts_left}")
        print(f"You lost. The number was {self.secret}.")
        return False
