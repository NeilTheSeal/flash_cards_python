class Turn:
    def __init__(self, guess, card):
        self.guess = guess
        self.card = card

    def correct(self):
        return self.guess == self.card.answer

    def feedback(self):
        if self.guess.lower() == self.card.answer.lower():
            return "Correct!"

        return f"Incorrect. The correct answer is {self.card.answer}."
