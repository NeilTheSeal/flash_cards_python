from flash_cards.card import Card


class CardGenerator:
    def __init__(self, file_path):
        self.cards = []
        self.file_text = ""
        self.file_path = file_path

    def parse_file(self):
        with open(self.file_path) as file:
            self.file_text = file.read()

    def push_cards(self):
        for card in self.file_text.split("\n"):
            question, answer, category = card.split(",")
            self.cards.append(Card(question, answer, category))
