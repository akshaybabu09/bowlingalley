from strategies import Strategies
from lane import Lane


class BowlingAlley:

    @staticmethod
    def bowling_game():

        new_strategy = input("Do you want to input a new strategy? (Answer with Yes or No)\n")
        if new_strategy.lower() == 'yes':
            num_of_strategy = int(input("Number of strategies you want to add:"))
            if num_of_strategy != 0:
                Strategies.add_strategy(num_of_strategy)
        Strategies.display_strategies()

        lanes = int(input("\nEnter the number of lanes: "))
        Lane.lanes = lanes
        Lane.start_game_lane()


BowlingAlley.bowling_game()
