import random

class Game():

    def initialize(self):
        self.random_value = random.randint(1, 10)
        print(self.random_value) #убрать перед игрой
        self.basic_validation()

    def type_validation(self):
        if self.input_value.isdigit():
            return True
        else:
            print('Ну рили? Ты не можешь цифру от чего-то другого отличить?')
            return False
    def range_validation(self):
        if int(self.input_value) >= 1 and int(self.input_value) <= 10:
            return True
        else:
            print('Тебе же сказали, числа только от 1 до 10!')
            return False

    def min_value_validation(self):
        if int(self.random_value) < int(self.input_value):
            print('Число, которое мы загадали, меньше')
            return False
        else:
            return True

    def max_value_validation(self):
        if int(self.random_value) > int(self.input_value):
            print('Число, которое мы загадали, больше')
            return False
        else:
            return True

    def win_validation(self):
        if int(self.random_value) == int(self.input_value):
            print('Кто молодец? Ты молодец!')
            return True

    def basic_validation(self):
        self.input_value = input('Введи число от 1 до 10\n') #можно было сделать int(input), но хотелось побаловаться с валидацией
        while True:
            if not self.type_validation():
                break
            if not self.range_validation():
                break
            if not self.min_value_validation():
                break
            if not self.max_value_validation():
                break
            if self.win_validation():
                return
        self.basic_validation()

x = Game()
x.initialize()


