import random

from player import Player


class Lane:

    lane_occupation = {}
    lanes = 0

    @staticmethod
    def start_game_lane():
        lanes = Lane.lanes
        for i in range(lanes):
            Lane.lane_occupation[i+1] = False
        Lane.team_game()

    @staticmethod
    def team_game():
        player_count = int(input("\nEnter number of Players in Team: "))

        lane = Lane.choose_random_lane()
        print("\nThe game will be held in lane {}.".format(lane))

        Player.fetch_player_details(player_count)
        Player.player_game()
        Player.display_player_details(lane)
        Lane.lane_occupation[lane] = False
        Lane.verify_next_game()

    @staticmethod
    def choose_random_lane():
        lane = random.choice(list(Lane.lane_occupation))
        if not Lane.lane_occupation[lane]:
            Lane.lane_occupation[lane] = True
            return lane
        return Lane.choose_random_lane()

    @staticmethod
    def verify_next_game():
        next_game = input("Start Another Game?\nPlease respond either Yes or No\n")
        if next_game.lower() == 'yes':
            Lane.start_game_lane()
