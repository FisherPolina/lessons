class Game():

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