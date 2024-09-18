class Deck:
    def __init__(self, cards):
        self.cards = cards

    def count(self):
        return len(self.cards)

    def cards_in_category(self, category):
        num_of_cards = 0
        for card in self.cards:
            if card.category == category:
                num_of_cards += 1
        return num_of_cards
