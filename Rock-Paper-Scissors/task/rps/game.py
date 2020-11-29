import random


class RockPaperScissors:
    def __init__(self):
        self.user_name_list, self.user_score_list = [], []
        self.user_score = 0
        self.user_name = input("Enter your name: ")
        print("Hello,", self.user_name)
        self.options_list = input()
        self.default_win_conditions = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
        self.winning_cases = {
            'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
            'water': ['scissors', 'fire', 'rock', 'gun', 'lightning', 'devil', 'dragon'],
            'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
            'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
            'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
            'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
            'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
            'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
            'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
            'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
            'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
            'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
            'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
            'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
            'devil': ['human', 'snake', 'scissors', 'fire', 'rock', 'gun', 'lightning']
        }

    def readfile(self):
        with open("rating.txt", "r") as file:
            for i in file:
                data = i.split(" ")
                self.user_name_list.append(data[0])
                self.user_score_list.append(data[1])

        self.user_score = int(self.user_score_list[self.user_name_list.index(self.user_name)])

    def basic(self):
        self.readfile()

        while True:
            option = input()
            comp_selected = random.choice(["rock", "paper", "scissors"])
            if option == "!exit":
                exit("Bye!")
            elif option == "!rating":
                print(f'Your rating: {self.user_score}')
            elif option in self.default_win_conditions:
                if option == comp_selected:
                    print(option)
                    self.user_score += 50
                    print(f'There is a draw ({option})')
                elif self.default_win_conditions[option] == comp_selected:
                    # print(self.default_win_conditions[option])
                    self.user_score += 100
                    print(f'Well done. The computer chose {comp_selected} and failed')
                else:
                    # print(self.default_win_conditions[option])
                    print(f'Sorry, but the computer chose {comp_selected}')
            else:
                print('Invalid input')

    def advanced(self):
        self.readfile()

        while True:
            option = input()
            comp_selected = random.choice(["rock", "paper", "scissors", "water", "dragon", "devil",
                                           "lightning", "gun", "fire", "snake", "human", "tree", "wolf", "sponge",
                                           "air"])
            if option == "!exit":
                exit("Bye!")
            elif option == "!rating":
                print(f'Your rating: {self.user_score}')
            elif option in self.winning_cases:
                if option == comp_selected:
                    # print(option)
                    self.user_score += 50
                    print(f'There is a draw ({option})')
                elif comp_selected in self.winning_cases[option]:
                    # print(self.winning_cases[option])
                    self.user_score += 100
                    print(f'Well done. The computer chose {comp_selected} and failed')
                else:
                    # print(self.winning_cases[option])
                    print(f'Sorry, but the computer chose {comp_selected}')
            else:
                print('Invalid input')

    def make_decision(self):
        if self.options_list is not '':
            print("Okay, let's start")
            self.advanced()
        else:
            print("Okay, let's start")
            self.basic()


if __name__ == "__main__":
    RockPaperScissors().make_decision()
