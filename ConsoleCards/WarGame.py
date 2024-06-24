# WarGame.py

from CardGameDeck import DeckOfCards, Card

class War:
    def __init__(self):
        self.deck = DeckOfCards()
        self.player1_hand, self.player2_hand = self.__deal_hand()

    def play(self):
        self.__battle()

    def __deal_hand(self):
        half_deck = len(self.deck.cards) // 2
        player1_hand = [self.deck.deal_card() for _ in range(half_deck)]
        player2_hand = [self.deck.deal_card() for _ in range(half_deck)]
        return player1_hand, player2_hand

    def __battle(self):
        player1_pile = []
        player2_pile = []
        player1_score = 0
        player2_score = 0
        ties = 0

        while len(self.player1_hand) > 0 or len(self.player2_hand) > 0:
            if len(self.player1_hand) == 0:
                random.shuffle(player1_pile)
                self.player1_hand = player1_pile.copy()
                player1_pile.clear()

            if len(self.player2_hand) == 0:
                random.shuffle(player2_pile)
                self.player2_hand = player2_pile.copy()
                player2_pile.clear()

            card1 = self.player1_hand.pop()
            card2 = self.player2_hand.pop()
            print(f"{card1} vs {card2}")

            if card1 > card2:
                player1_pile.append(card1)
                player1_pile.append(card2)
                player1_score += 1
                print(f"Player 1 wins with {card1}")

            elif card2 > card1:
                player2_pile.append(card1)
                player2_pile.append(card2)
                player2_score += 1
                print(f"Player 2 wins with {card2}")

            else:
                ties += 1
                print("Tie! Both players draw a card and play again")

        print("------------------------------------------")
        print("Game over!")
        print("------------------------------------------")
        print(f"Player 1: {player1_score}")
        print(f"Player 2: {player2_score}")
        print(f"Ties: {ties}")
        print("==========================================")

if __name__ == "__main__":
    game = War()
    game.play()
