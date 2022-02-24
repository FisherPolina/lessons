from Game import Game


class SecondGame(Game):

    def start_game(self) -> None:
        while True:
            self.nonrandom_value = ((self.min_value + self.max_value) // 2)
            print(f'Ты загадал число {self.nonrandom_value}?')
            self.help_input = input('Дай мне подсказку, твоё число < или > или = ?\n')
            if self.help_input == '=':
                print('Я молодец!')
                break
            elif self.help_input == '<':
                if not self.range_validation():
                    break
                print(f'{self.nonrandom_value} больше того, что ты загадал')
                self.max_value = (self.nonrandom_value) - 1
                self.nonrandom_value = ((self.min_value + self.max_value) // 2)
            elif self.help_input == '>':
                if not self.range_validation():
                    break
                print(f'{self.random_value} меньше того, что ты загадал')
                self.min_value = int(self.nonrandom_value) + 1
                self.nonrandom_value = ((self.min_value + self.max_value) // 2)
            else:
                print('Ты можешь выбрать только  < или > или =')
                break

SecondGame()