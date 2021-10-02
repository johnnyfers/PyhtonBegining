import random
import PySimpleGUI as sg

class DiceSimulator:
    def __init__(self):
        self.min_value = 1
        self.max_value = 6
        self.message = 'do u want to generate another value? (yes/no)'
        
        self.layout = [
            [sg.Text('Shoot the dice?')],
            [sg.Button('yes'), sg.Button('no')]
        ]

    def main(self):
        self.window = sg.Window('Dice Simulator', layout=self.layout)
        
        self.events, self.values = self.window.read()
        
        try:
            if self.events == 'yes':
                self.generateDiceValue()
            elif self.events == 'no':
                print('thanks for using it :)')
            else:
                print('invalid input')
        except:
            print('system error')
    
    def generateDiceValue(self):
        print(random.randint(self.min_value, self.max_value))

simulator = DiceSimulator()

simulator.main()
