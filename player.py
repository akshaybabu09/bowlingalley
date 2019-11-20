

class Player:

    players = {}

    def __init__(self, name):
        self.pid = 0
        self.name = name

    @staticmethod
    def fetch_player_details(players_count):
        pid = 0
        for i in range(players_count):
            name = input("Enter the Player" + str(i+1) + " Name: ")
            pid += 1
            Player.players[pid] = {
                'pid': pid,
                'name': name
            }
        print("\n")

    @staticmethod
    def player_game():
        from individual_game import Game
        players = Player.players

        for player in players:
            Game.bowling_game(players[player]['pid'])

    @staticmethod
    def calculate_final_score(pid):
        total_score = 0
        players = Player.players
        game_scores = players[pid]['game_scores']
        for set_score in game_scores:
            total_score += set_score['set_total_score']
        players[pid]['game_score'] = total_score

    @staticmethod
    def display_player_details():
        players = Player.players
        for player in players:
            print("Id: {}, Name: {}, Score: {}".format(
                players[player]['pid'], players[player]['name'], players[player]['game_score'])
            )
        winner_name = Player.find_game_winner()
        print("\nWinner is {}".format(winner_name))
        view_details = input("\nDo you want to view score details of each player? (Answer with a Yes or a No)\n")
        if view_details.lower() == 'yes':
            Player.display_detailed_score()

    @staticmethod
    def find_game_winner():
        players = Player.players
        player_scores = [players[player]['game_score'] for player in players]
        max_index = player_scores.index(max(player_scores))
        for player in players:
            if players[player]['pid'] == max_index + 1:
                return players[player]['name']

    @staticmethod
    def display_detailed_score():
        players = Player.players
        for player in players:
            player_set_data = players[player]['game_scores']
            count = 0
            for set_data in player_set_data:
                count += 1
                Player.print_set_data(count, len(player_set_data), set_data)
            print("Final Score: {}\n".format(players[player]['game_score']))

    @staticmethod
    def print_set_data(game_set, total_sets, set_data):
        print("Set {}:\n".format(game_set))
        trial_1 = set_data.get('trial_1')
        trial_2 = set_data.get('trial_2')
        trial_3 = set_data.get('trial_3')

        print("Trial 1: {}".format(trial_1))
        if trial_1 != 10:
            print("Trial 2: {}".format(trial_2))
        if game_set == total_sets and (trial_1 == 10 or (trial_1 + trial_2) == 10):
            print("Trial 3: {}".format(trial_3))
        print("Set outcome: {} \n".format(set_data.get('set_total_score')))


