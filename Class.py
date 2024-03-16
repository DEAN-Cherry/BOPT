from random import shuffle


class Card:
    def __init__(self, suit: list, rank: str, value: int):
        self._value = value
        self._suit = suit
        self._rank = rank

    def get_value(self):
        return self._value

    def get_suit(self):
        return self._suit

    def get_rank(self):
        return self._rank

    def set_value(self, value: int):
        self._value = value

    def set_suit(self, suit: str):
        self._suit = suit

    def set_rank(self, rank: str):
        self._rank = rank

    def __str__(self):
        return self._rank + " of " + str(self._suit)


class Deck:
    def __init__(self, deck=None):
        self._cards = []
        self._cards_now = []
        self.build(deck)

    def build(self, deck=None):
        if deck is None:
            suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
            ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen',
                     'King', 'Ace']
            values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
            for suit in suits:
                for i in range(13):
                    card = Card([suit], ranks[i], values[i])
                    self._cards.append(card)
        else:
            self._cards = deck
        self._cards_now = self._cards

    def get_cards(self):
        return self._cards

    def set_cards(self, cards: list):
        self._cards = cards

    def get_cards_now(self):
        return self._cards_now

    def shuffle(self):
        self._cards_now = self._cards
        shuffle(self._cards_now)

    def deal(self):
        return self._cards_now.pop()

    def add_card(self, card: Card):
        self._cards.append(card)

    def del_card(self, card: Card):
        self._cards.remove(card)


class Hand:
    def __init__(self, upper_limit: int):
        self._cards = []
        self._upper_limit = upper_limit

    def add_card(self, card: Card):
        self._cards.append(card)

    def get_cards(self):
        return self._cards

    def __str__(self):
        return str(self._cards)

    # 弃牌
    def discard(self, card: Card, deck: Deck):
        self._cards.remove(card)
        self.add_card(deck.deal())
