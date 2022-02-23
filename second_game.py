from random import randint
from Game import Game


class SecondGame(Game):
    def __init__(self):
        self.min_value = 1
        self.max_value = 10
        self.random_value = randint(self.min_value, self.max_value)
        self.input_value = input('Загадай число от 1 до 10\n')
        self.start_game()


    def start_game(self) -> None:
        while True:
            if not self.data_validator():
                break
            print(f'Ты загадал число {self.random_value}?')
            help_input = input('Дай мне подсказку, твоё число < или > или = ?\n')
            if help_input == '=':
                print('Я молодец!')
                break
            elif help_input == '<':
                print(f'{self.random_value} больше того, что ты загадал')
                self.max_value = (self.random_value) - 1
                self.random_value = randint(self.min_value, self.max_value)
            elif help_input == '>':
                print(f'{self.random_value} меньше того, что ты загадал')
                self.min_value = int(self.random_value) + 1
                self.random_value = randint(self.min_value, self.max_value)
            else:
                print('Ты можешь выбрать только  < или > или =')
                break

SecondGame()