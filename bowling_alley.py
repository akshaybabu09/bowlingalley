from player import Player
from strategies import Strategies


class BowlingAlley:

    @staticmethod
    def bowling_game():

        new_strategy = input("Do you want to input a new strategy? (Answer with Yes or No)\n")
        if new_strategy.lower() == 'yes':
            num_of_strategy = int(input("Number of strategies you want to add:"))
            if num_of_strategy != 0:
                Strategies.add_strategy(num_of_strategy)

        player_count = int(input("Enter number of Players: "))
        print("\n")

        Player.fetch_player_details(player_count)
        Player.player_game()
        Player.display_player_details()


BowlingAlley.bowling_game()
