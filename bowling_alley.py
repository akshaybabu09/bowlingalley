class Player:

    @staticmethod
    def player_game():

        min_value = 0
        total_score = 0
        total_sets = 10
        for game_set in range(total_sets):

            trial_1, trial_2, trial_3 = TrialSet.set_score(min_value, total_sets, game_set)
            score = trial_1 + trial_2 + trial_3

            bonus = 0
            if trial_1 == 10:
                bonus += 10
            if trial_1 + trial_2 == 10:
                bonus += 5

            set_total_score = score + bonus
            Player.print_set_data(game_set, total_sets, trial_1, trial_2, trial_3, set_total_score)
            total_score += set_total_score
        return total_score

    @staticmethod
    def print_set_data(game_set, total_sets, trial_1, trial_2, trial_3, set_total_score):
        print("Set {}:\n".format(game_set + 1))
        print("Trial 1: {}\n".format(trial_1))
        if trial_1 != 10:
            print("Trial 2: {}\n".format(trial_2))
        if game_set == (total_sets - 1) and (trial_1 == 10 or (trial_1 + trial_2) == 10):
            print("Trial 3: {}\n".format(trial_3))
        print("Set outcome: {} \n".format(set_total_score))


class TrialSet:

    @staticmethod
    def set_score(min_value, total_sets, game_set):
        trial_1 = TrialSet.generator(total_sets, min_value)
        trial_2 = 0
        trial_3 = 0

        if trial_1 == 10:
            return trial_1, trial_2, trial_3

        trial_2 = TrialSet.generator(total_sets, trial_1)

        if game_set == (total_sets + 1) and (trial_1 == 10 or (trial_1 + trial_2) == 10):
            trial_3 = TrialSet.generator(total_sets, min_value)
            return trial_1, trial_2, trial_3

        return trial_1, trial_2, trial_3

    @staticmethod
    def generator(total_sets, trial):
        from random import randint
        return randint(0, total_sets - (trial % total_sets))


final_score = Player.player_game()
print("Total Score = {}".format(final_score))
