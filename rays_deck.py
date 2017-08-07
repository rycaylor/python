
class Deck(object):
    def __init__(self):
        cards = [2,3,4,5,6,7,8,9,10,'A','J','Q','K']
        suit = ['Spades','Rock','Paper','Scissor']
        deck = []
        for i in range(0,len(suit)):
            for j in range(0,len(cards)):
                deck.append([suit[i],cards[j]])
        self.deck = deck

    def draw(self):
        drawn = self.deck.pop()
        return drawn

    def getback(self,card):
        self.deck.append(card)


class Ray(object):
    def __init__(self):
        self.name = 'Ray'
        self.hand = []

    def getshorty(self,deck):
        card = deck.draw()
        self.hand.append(card)
        print self.hand
        return self

    def discard(self,deck):
        bye = self.hand.pop()
        deck.getback(bye)
        print self.hand
        return self




ray = Deck()
joe = Ray()

joe.getshorty(ray).getshorty(ray).getshorty(ray).discard(ray).discard(ray).getshorty(ray)
