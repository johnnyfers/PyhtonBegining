import random

class DiceSimulator:
    def __init__(self):
        self.min_value = 1
        self.max_value = 6
        self.message = 'do u want to generate another value? (yes/no)'
    
    def main(self):
        answer = input(self.message)
        
        try:
            if answer == 'yes':
                self.generateDiceValue()
            elif answer == 'no':
                print('thanks for using it :)')
            else:
                print('invalid input')
        except:
            print('system error')
    
    def generateDiceValue(self):
        print(random.randint(self.min_value, self.max_value))

simulator = DiceSimulator()

simulator.main