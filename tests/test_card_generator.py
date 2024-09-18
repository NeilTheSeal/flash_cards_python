from flash_cards.card import Card
from flash_cards.card_generator import CardGenerator


class TestCardGenerator:
    card_generator = CardGenerator("cards.txt")

    def test_it_exists(self):
        assert isinstance(TestCardGenerator.card_generator, CardGenerator)

    def test_if_parses(self):
        self.card_generator.parse_file()
        assert self.card_generator.file_text.startswith("What is 10 + 15?")

    def test_if_pushes(self):
        self.card_generator.parse_file()
        self.card_generator.push_cards()
        assert len(TestCardGenerator.card_generator.cards) == 7
        for card in self.card_generator.cards:
            assert isinstance(card, Card)
            assert card.question
            assert card.answer
