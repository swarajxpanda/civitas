import random


class Civilization:
    def __init__(self, name):

        self.name = name

        self.resources = 100.0
        self.military = 50.0
        self.population = 100.0
        self.territory = 1

        # AI personality weights
        self.aggression = random.uniform(
            0, 1
        )  # learn: generates random floating point number
        self.trade_preference = random.uniform(0, 1)
        self.expansionism = random.uniform(0, 1)

    def calculate_scores(self, enemy):

        attack_score = self.aggression * 100 + (self.military - enemy.military)

        trade_score = self.trade_preference * 100 + self.resources * 0.3

        expand_score = self.expansionism * 100 + self.resources * 0.2

        gather_score = 50

        return {
            "ATTACK": attack_score,
            "TRADE": trade_score,
            "EXPAND": expand_score,
            "GATHER": gather_score,
        }

    def choose_action(self, enemy):

        scores = self.calculate_scores(enemy)
        action = max(
            scores, key=scores.get
        )  # learn: max() finds the largest item, key=scores.get tells max() to compare dictionary values instead of dictionary keys

        return action, scores
