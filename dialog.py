import time
import os

class Dialog:

    def __init__(self, question):
        self.question = question
        self.option_names = []
        self.option_functions = []

    def setOptions(self, *args):
        for option in args:
            self.option_names.append(option[0])
            self.option_functions.append(option[1])

    def show(self):
        print(self.question)
        for option_name in self.option_names:
            print(f"[{self.option_names.index(option_name)}] {option_name}")
        try:
            self.option_index = int(input("Enter the number you want to select: "))
        except:
            print("Your input is invalid!")
            time.sleep(1)
            os.system('cls')
            self.show()
        
        for option_name in self.option_names:
            if self.option_index == self.option_names.index(option_name):
                print(f"-> You chose option '{option_name}'")
                time.sleep(1)
                self.option_functions[self.option_names.index(option_name)]()
            elif self.option_index < 0 or self.option_index > self.option_names.index(self.option_names[-1]):
                print("Your input is out of range...")
                time.sleep(1)
                os.system('cls')
                self.show()
        