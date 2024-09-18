from flash_cards.round import Round
from flash_cards.deck import Deck
from flash_cards.card import Card
from flash_cards.turn import Turn


class TestRound:
    card1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
    card2 = Card(
        "The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?",
        "Mars",
        "STEM",
    )
    card3 = Card(
        "Describe in words the exact direction that is 697.5° clockwise from due north?",
        "North north west",
        "STEM",
    )
    cards = [card1, card2, card3]
    deck = Deck(cards)
    round = Round(deck)

    def define_round(self):
        self.round = Round(self.deck)

    def test_has_deck_attribute(self):
        self.define_round()
        assert isinstance(self.round.deck, Deck)

    def test_has_turns_attribute(self):
        self.define_round()
        assert not self.round.turns

    def test_has_current_card_method(self):
        self.define_round()
        assert self.round.current_card() == self.card1

    def test_adds_turn_object(self):
        self.define_round()
        new_turn = self.round.take_turn("Juneau")
        assert isinstance(new_turn, Turn)
        assert self.round.turns == [new_turn]

    def test_shows_answer_is_correct(self):
        self.define_round()
        new_turn = self.round.take_turn("Juneau")
        assert new_turn.correct() is True

    def test_shows_answer_is_incorrect(self):
        self.define_round()
        new_turn = self.round.take_turn("Anchorage")
        assert new_turn.correct() is False

    def test_appends_turn_to_list(self):
        self.define_round()
        self.round.take_turn("Juneau")
        self.round.take_turn("Anchorage")
        assert len(self.round.turns) == 2

    def test_displays_number_correct(self):
        self.define_round()
        self.round.take_turn("Juneau")
        self.round.take_turn("Mars")
        assert self.round.number_correct == 2

    def test_gives_feedback_on_last_answer(self):
        self.define_round()
        self.round.take_turn("Juneau")
        assert self.round.turns[-1].feedback() == "Correct!"
        self.round.take_turn("Pluto")
        assert (
            self.round.turns[-1].feedback() == "Incorrect. The correct answer is Mars."
        )

    def test_doesnt_count_every_answer_as_correct(self):
        self.define_round()
        self.round.take_turn("Juneau")
        self.round.take_turn("Pluto")
        assert self.round.number_correct == 1

    def test_shows_percent_correct_for_category(self):
        self.define_round()
        self.round.take_turn("Juneau")
        self.round.take_turn("Mars")
        self.round.take_turn("Northeast")
        assert self.round.percent_correct_by_category("Geography") == 100
        assert self.round.percent_correct_by_category("STEM") == 50

    def test_shows_current_turn_card(self):
        self.define_round()
        assert self.round.current_card() == self.card1
        self.round.take_turn("Juneau")
        assert self.round.current_card() == self.card2
        self.round.take_turn("Mars")
        assert self.round.current_card() == self.card3
