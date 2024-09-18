from flash_cards.deck import Deck
from flash_cards.card import Card


class TestDeck:
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

    def test_exists(self):
        assert isinstance(self.deck, Deck)

    def test_cards_is_list(self):
        assert isinstance(self.deck.cards, list)

    def test_correct_cards(self):
        assert self.deck.cards == self.cards

    def test_count(self):
        assert self.deck.count() == 3

    def test_cards_in_category(self):
        assert self.deck.cards_in_category("STEM") == 2
        assert self.deck.cards_in_category("Geography") == 1
        assert self.deck.cards_in_category("Pop Culture") == 0
