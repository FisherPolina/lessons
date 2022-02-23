from random import randint
from Game import Game


class SecondGame(Game):

    def start_game(self) -> None:
        while True:
            print(f'Ты загадал число {self.random_value}?')
            self.help_input = input('Дай мне подсказку, твоё число < или > или = ?\n')
            if self.help_input == '=':
                print('Я молодец!')
                break
            elif self.help_input == '<':
                if not self.limit_validation():
                    break
                print(f'{self.random_value} больше того, что ты загадал')
                self.max_value = (self.random_value) - 1
                self.random_value = randint(self.min_value, self.max_value)
            elif self.help_input == '>':
                if not self.limit_validation():
                    break
                print(f'{self.random_value} меньше того, что ты загадал')
                self.min_value = int(self.random_value) + 1
                self.random_value = randint(self.min_value, self.max_value)
            else:
                print('Ты можешь выбрать только  < или > или =')
                break

SecondGame()