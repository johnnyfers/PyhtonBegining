import random
import PySimpleGUI as sg


class GuessTheNumber:
    def __init__(self):
        self.random_value = 0
        self.min_value = 1
        self.max_value = 100
        self.try_again = True

        self.layout = [
            [sg.Text('value:', size=(30, 0))],
            [sg.Input(size=(28, 0), key='value')],
            [sg.Button('shoot!')],
            [sg.Output(size=(30, 10))]
        ]

    def main(self):
        self.window = sg.Window('guess the number', layout=self.layout)

        self.generateRandomNumber()

        try:
            self.ask()

            while self.try_again == True:
                if int(self.value) > self.random_value:
                    print('guess a lower number')
                    
                    self.ask()
                elif int(self.value) < self.random_value:
                    print('guess a higher number')
                    
                    self.ask()
                else:
                    self.try_again = False
                    print('you guessed the right number!!!')
        except:
            print('something went wrong, try again')
            self.main()
    
    def ask(self):
            self.events, self.values = self.window.read()
            self.value = self.values['value']
            
    def generateRandomNumber(self):
        self.random_value = random.randint(self.min_value, self.max_value)

GuessTheNumber().main()
