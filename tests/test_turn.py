from flash_cards.turn import Turn
from flash_cards.card import Card


class TestTurn:
    card = Card("What is the capital of Alaska?", "Juneau", "Geography")
    turn = Turn("Juneau", card)

    def test_exists(self):
        assert isinstance(self.turn, Turn)

    def test_has_guess(self):
        assert self.turn.guess == "Juneau"

    def test_has_card(self):
        assert self.turn.card == self.card

    def test_correct(self):
        assert self.turn.correct() is True

    def test_incorrect(self):
        turn = Turn("Anchorage", self.card)
        assert turn.correct() is False

    def test_feedback_correct(self):
        assert self.turn.feedback() == "Correct!"

    def test_feedback_incorrect(self):
        turn = Turn("Anchorage", self.card)
        assert turn.feedback() == "Incorrect. The correct answer is Juneau."
