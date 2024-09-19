from collections import Counter
from itertools import combinations

class Game():

    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1, player2):
        def top3():
            top_three = self.registry.most_common(3)
            for player, score in top_three:
                print(f"{player} {score}")

        player1.reset()
        player2.reset()

        for _ in range(self.matches):
            action1 = player1.decide(player2.history)
            action2 = player2.decide(player1.history)

            player1.history.append(action1)
            player2.history.append(action2)

            if action1 == action2 == 'cooperate':
                self.registry[player1.name]+=2
                self.registry[player2.name]+=2
            elif action1 == 'cheat' and action2 == 'cooperate':
                self.registry[player1.name]+=3
                self.registry[player2.name]-=1
            elif action1 == 'cooperate' and action2 == 'cheat':
                self.registry[player1.name]-=1
                self.registry[player2.name]+=3
        return top3

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.history = []

    def reset(self):
        self.history = []

    def decide(self, history):
        pass


class Cheater(Player):
    def decide(self,history):
        return 'cheat'

class Cooperator(Player):
    def decide(self, history):
        return 'cooperate'

class Copycat(Player):
    def decide(self, history):
        if self.history == []:
            solution = 'cooperate'
        else:
            solution = history[-1]
        return solution

class Grudger(Player):
    def decide(self, history):
        if history and 'cheat' in history:
            solution = 'cheat'
        else: 
            solution = 'cooperate'
        return solution

class Detective(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.first_moves = ['cooperate', 'cheat', 'cooperate', 'cooperate']
        self.move_index = 0

    def reset(self):
        self.move_index = 0
        self.history = []

    def decide(self, history):
        if self.move_index < len(self.first_moves):
            solution = self.first_moves[self.move_index]
            self.move_index+=1
        elif 'cheat' in history[:4]:
            solution = history[-1]
        else:
            solution = 'cheat'
        return solution

def main():
    players = [
        Copycat("Copycat"),
        Cheater("Cheater"),
        Cooperator("Cooperator"),
        Grudger("Grudger"),
        Detective("Detective"),
    ]

    game = Game(matches=10)
    pairs = list(combinations(players, 2))
    for pair in pairs:
        player1, player2 = pair[0], pair[1]
        top3 = game.play(player1, player2)
    top3()
    
if __name__ == "__main__":
    main()
