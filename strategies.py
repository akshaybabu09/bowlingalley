class Strategies:

    strategies = {
        "strike": {
            "condition": "trial_1 == 10",
            "bonus": 10
        },
        "spare": {
            "condition": "(trial_1 + trial_2) == 10",
            "bonus": 5
        }
    }

    def __init__(self, name, condition, bonus):
        self.name = name
        self.condition = condition
        self. bonus = bonus
        self.strategies[name] = {
            "condition": self.condition,
            "bonus": self.bonus
        }

    @staticmethod
    def run_strategy(trial_1, trial_2):
        strategies = Strategies.strategies
        for strategy in strategies:
            if eval(strategies[strategy]['condition']):
                return strategies[strategy]['bonus']

        return 0

    @staticmethod
    def add_strategy(num_of_strategy):
        for i in range(num_of_strategy):
            name = input("Enter the name of strategy: ")
            condition = input("Enter the condition for the strategy: \nExample: trial_1 + trial_2 == 10\n")
            bonus_value = int(input("Enter the value of bonus: "))
            Strategies(name, condition, bonus_value)
        print(Strategies.strategies)
