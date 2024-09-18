from time import sleep
from flash_cards.deck import Deck
from flash_cards.round import Round
from flash_cards.card_generator import CardGenerator


class Game:
    def __init__(self):
        card_generator = CardGenerator("cards.txt")
        card_generator.parse_file()
        card_generator.push_cards()
        self.cards = card_generator.cards
        self.deck = Deck(self.cards)
        self.round = Round(self.deck)

    def start(self):
        print(f"Welcome! You're playing with {len(self.cards)} cards.")
        self.quiz_loop()

    def provide_question(self):
        print(
            f"This is card number {self.round.turn_number + 1} out of {len(self.cards)}."
        )
        print(f"Question: {self.round.current_card().question}")

    def provide_feedback(self, turn):
        print(turn.feedback())
        sleep(1)
        print("--------------------------------------\n")

    def take_input(self):
        self.provide_question()
        guess = input()
        turn = self.round.take_turn(guess)
        self.provide_feedback(turn)

    def quiz_loop(self):
        while self.round.turn_number < self.deck.count():
            self.take_input()
        self.show_results()

    def categories_array(self):
        categories = []
        for card in self.deck.cards:
            if card.category not in categories:
                categories.append(card.category)
        return categories

    def show_results(self):
        print("****** Game over! ******")
        print(
            f"You had {self.round.number_correct} correct guesses out of {len(self.cards)} for a total score of {round(100 * self.round.number_correct / self.deck.count())}%."
        )
        for category in self.categories_array():
            print(
                f"{category} - {self.round.percent_correct_by_category(category)}% correct"
            )
        print("****** Game over! ******")
        sleep(1)
        print("Would you like to play again? (yes/no)")
        answer = input()
        if answer == "yes":
            self.round = Round(self.deck)
            self.start()
        else:
            print("Goodbye!")
            sleep(1)
            return
