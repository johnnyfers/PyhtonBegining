import random

class GuessTheNumber:
    def __init__(self):
        self.random_value = 0
        self.min_value = 1
        self.max_value = 100
        self.try_again

    def main(self):
        self.generateRandomNumber()
        self.ask()

        while self.try_again == true:
            if int(self.value) > self.random_value:
                print('choose a lower number')
                
                self.ask()
            elif int(self.value) < self.random_value:
                print('choose a higher number')
                
                self.ask()
            else:
                self.try_again = false
                print('you guessed the right number!!!')

    def ask(self):
        self.value = input('guess the number: ')

    def generateRandomNumber(self):
        self.random_value = random.randint(self.min_value, self.max_value)

GuessTheNumber().main()