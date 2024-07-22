import random

class Deck():
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        random.shuffle(self.card_list)
        self.current_card = 0
        self.size = size

    def deal(self):
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
            print('Reshuffling...!!!')
        self.current_card += 1
        return  self.card_list[self.current_card - 1]

def poker_game():
    # Initialize a deck of 52 cards
    deck = Deck(52)

    # Deal an initial hand of five cards
    hand = [deck.deal() for _ in range(5)]
    print(f"Initial hand: {hand}")

    while True:
        try:
            # Prompt the user to enter a series of numbers to select cards to be replaced
            positions_to_replace = input("Enter positions of cards to replace (1-5, separated by commas): ")
            positions_to_replace = list(map(int, positions_to_replace.split(',')))

            # Validate the positions
            if any(pos < 1 or pos > 5 for pos in positions_to_replace):
                raise ValueError("Positions must be between 1 and 5.")

            # Replace the selected cards
            for pos in positions_to_replace:
                hand[pos-1] = deck.deal()

            print(f"Final hand after drawing new cards: {hand}")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

# Run the poker game
poker_game()
