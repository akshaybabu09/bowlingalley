from player import Player
from strategies import Strategies


class Game:

    @staticmethod
    def individual_bowling_game(pid):

        min_value = 0
        total_sets = 10
        trial_3 = 0
        game_scores = []
        for game_set in range(total_sets):
            if game_set == total_sets - 1:
                trial_1, trial_2, trial_3 = Game.set_score(min_value, total_sets, game_set)
                score = trial_1 + trial_2 + trial_3
            else:
                trial_1, trial_2 = Game.set_score(min_value, total_sets, game_set)
                score = trial_1 + trial_2

            bonus = Strategies.run_strategy(trial_1, trial_2)

            set_total_score = score + bonus

            if game_set == (total_sets - 1) and (trial_1 == 10 or (trial_1 + trial_2) == 10):
                trial_scores = Game.three_trail_set(trial_1, trial_2, trial_3, set_total_score)
            else:
                trial_scores = Game.two_trail_set(trial_1, trial_2, set_total_score)

            game_scores.append(trial_scores)
        Player.players[pid]['game_scores'] = game_scores
        Player.calculate_final_score(pid)

    @staticmethod
    def set_score(min_value, total_sets, game_set):
        trial_1 = Game.generator(total_sets, min_value)
        trial_3 = 0

        trial_2 = Game.generator(total_sets, trial_1)

        if game_set == (total_sets - 1):
            if (trial_1 == 10) or ((trial_1 + trial_2) == 10):
                trial_3 = Game.generator(total_sets, min_value)
            return trial_1, trial_2, trial_3

        return trial_1, trial_2

    @staticmethod
    def generator(total_sets, trial):
        from random import randint
        return randint(0, total_sets - trial)

    @staticmethod
    def three_trail_set(trial_1, trial_2, trial_3, set_total_score):
        return {
                    "trial_1": trial_1,
                    "trial_2": trial_2,
                    "trial_3": trial_3,
                    "set_total_score": set_total_score
                }

    @staticmethod
    def two_trail_set(trial_1, trial_2, set_total_score):
        return {
                    "trial_1": trial_1,
                    "trial_2": trial_2,
                    "set_total_score": set_total_score
                }
