from flash_cards.turn import Turn


class Round:
    def __init__(self, deck):
        self.deck = deck
        self.turns = []
        self.turn_number = 0
        self.number_correct = 0

    def current_card(self):
        return self.deck.cards[self.turn_number]

    def take_turn(self, guess):
        turn = Turn(guess, self.current_card())
        self.turns.append(turn)
        self.turn_number += 1
        if turn.correct():
            self.number_correct += 1
        return turn

    def correct(self):
        return self.turns[-1].correct()

    def number_correct_by_category(self, category):
        count_correct = 0
        for turn in self.turns:
            if turn.card.category == category and turn.correct():
                count_correct += 1
        return count_correct

    def total_in_category(self, category):
        count_category = 0
        for turn in self.turns:
            if turn.card.category == category:
                count_category += 1
        return count_category

    def percent_correct_by_category(self, category):
        return round(
            (
                (
                    self.number_correct_by_category(category)
                    / self.total_in_category(category)
                )
                * 100
            )
        )
