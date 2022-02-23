from Game import Game
from random import randint

class FirstGame(Game):
    def __init__(self):
        self.min_value = 1
        self.max_value = 10
        self.random_value = randint(self.min_value, self.max_value)
        self.start_game()

    def start_game(self) -> None:
        self.input_value = input('Введи число от 1 до 10\n')  # можно было сделать int(input), но хотелось побаловаться с валидацией
        while True:
            if not self.data_validator():
                break
            if int(self.input_value) < self.random_value:
                print(f'{self.input_value} меньше того, что я загадал')
                break
            if int(self.input_value) > self.random_value:
                print(f'{self.input_value} больше того, что я загадал')
                break
            if int(self.input_value) == self.random_value:
                print(f'Поздравляю, я загадал именно {self.input_value}')
            return
        self.start_game()


FirstGame()