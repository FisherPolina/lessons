from random import randint
from Game import Game


class SecondGame(Game):


    def start_game(self) -> None:
        self.input_value = input('Загадай число от 1 до 10\n')
        while True:
            print(f'Ты загадал число {self.random_value}?')
            help_input = input('Дай мне подсказку, загаданное число < или > или = ?\n')
            if help_input == '=':
                print('Я молодец!')
            elif help_input == '<':
                print(f'{self.random_value} меньше того, что ты загадал')
                self.min_value = self.random_value
                self.random_value = randint(self.min_value, self.max_value)
                return
            elif help_input == '>':
                print(f'{self.random_value} больше того, что ты загадал')
                self.max_value = self.random_value
                self.random_value = randint(self.min_value, self.max_value)
                return
        self.start_game()

SecondGame()