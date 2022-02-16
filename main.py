from random import randint

class Game():

    def __init__(self):
        self.random_value = randint(1, 10)
        print(self.random_value) #убрать перед игрой
        self.basic_validation()
        
    def __del__(self):
        print('Game over')
    
    def data_validator(self) -> bool:
        if self.input_value.isdigit():
            self.input_value = int(self.input_value)
            if 1 <= self.input_value <= 10:
                return True
            else:
                print('Тебе же сказали, числа только от 1 до 10!')
                return False
        else:
            print('Ну рили? Ты не можешь цифру от чего-то другого отличить?')
            return False

    def start_game(self) -> None:
        self.input_value = input('Введи число от 1 до 10\n') #можно было сделать int(input), но хотелось побаловаться с валидацией
        while True:
            if not self.data_validator():
                break
            if self.input_value < self.random_value:
                print(f'{self.input_value} меньше того, что я загадал')
                break
            if self.input_value > self.random_value:
                 print(f'{self.input_value} больше того, что я загадал')
                break
            if self.input_value == self.random_value:
                 print(f'Поздравляю, я загадал именно {self.input_value}')
                return
        self.start_game()

Game()

