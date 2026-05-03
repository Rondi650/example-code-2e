import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]



Card.suit_values = dict(spades=3, hearts=2,
                        diamonds=1, clubs=0)                
def spades_high(card):                                      
    rank_value = FrenchDeck.ranks.index(card.rank)                
    suit_value = card.suit_values[card.suit]
    return rank_value * len(card.suit_values) + suit_value

Card.overall_rank = spades_high                             
lowest_card = Card('2', 'clubs')
highest_card = Card('A', 'spades')
print(Card.__dict__)                                  

print(highest_card)

print(FrenchDeck.__annotations__)