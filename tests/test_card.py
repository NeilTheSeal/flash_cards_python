from flash_cards.card import Card


def test_card():
    card = Card("What is the capital of Alaska?", "Juneau", "Geography")
    assert card.question == "What is the capital of Alaska?"
    assert card.answer == "Juneau"
    assert card.category == "Geography"
