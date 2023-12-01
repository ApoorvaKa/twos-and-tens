
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.is_hidden = False

    def __repr__(self):
        royals = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
        if self.is_hidden:
            return "Hidden"
        if self.value in royals:
            return f"{royals[self.value]} of {self.suit}"            
        return f"{self.value} of {self.suit}"
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __le__(self, other):
        return self.value <= other.value
    
    def is_bomb(self):
        return self.value == 10

    def is_reset(self):
        return self.value == 2
    
    def is_skip(self):
        return self.value == 3

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in range(2, 15):
                self.cards.append(Card(suit, value))
    
    def print_deck(self):
        for card in self.cards:
            print(card)


class Game:
    def __init__(self):
        self.deck = Deck()

def main():
    deck = Deck()
    deck.print_deck()


if __name__ == "__main__":
    main()