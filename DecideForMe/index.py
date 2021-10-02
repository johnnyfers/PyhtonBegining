import random

class DecideForMe:
    def __init__(self):
        self.answers = [
            'you should do that',
            'thats totally up to you',
            'please, dont do that',
            'not the right time to do it'
        ]
        
    def main(self):
        input('make a question: ')
        print(random.choice(self.answers))

DecideForMe().main()