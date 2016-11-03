from core import Command
import core
import random
import os
from time import sleep

class disarm(Command):
    def __init__(self, name="disarm", brief="Bomb disarming utility", privileges="root"):
        super(disarm, self).__init__(name=name, brief=brief, privileges=privileges)
        self.alias = ["disarm"]

    def runcmd(self, args):
        os.system("clear")
        if not core.armed:
            print("Bomb is not currently armed.")
            return
        if core.crypto1Locked or core.crypto2Locked:
            print("Both crypto locks must be unlocked")
            print("Crypto1Lock:", core.crypto1Locked)
            print("Crypto2Lock:", core.crypto2Locked)
            return
        self.print_vamPYre()
        self.disarming_utility(4)
        self.print_vamPYre()
        self.disarming_utility(5)
        self.print_vamPYre()
        self.disarming_utility(6)
        print("DISARMED")
        core.armed = False

    def print_vamPYre(self):
        vamPYre ="""
                       _______     __
                      |  __ \ \   / /
 __   ____ _ _ __ ___ | |__) \ \_/ / __ ___
 \ \ / / _` | '_ ` _ \|  ___/ \   / '__/ _ \\
  \ V / (_| | | | | | | |      | || | |  __/
   \_/ \__,_|_| |_| |_|_|      |_||_|  \___|
                ------Cyber Lockpick Utility

"""
        os.system("clear")
        print(vamPYre)

    def disarming_utility(self, size):
        self.size = size
        self.solution = []
        self.possibles = []
        self.roll_solution()
        self.guessed = ["-"]*self.size
        self.print_current()
        self.guessing()

    def roll_solution(self):
        character=""
        for i in range (0, self.size):
            character = self.rolling()
            while character in self.solution:
                character = self.rolling()
            self.solution.append(character)

        self.possibles = self.solution.copy()
        for i in range (0, self.size):
            character = self.rolling()
            while character in self.possibles:
                character = self.rolling()
            self.possibles.append(character)
        self.possibles.sort()


    def print_current(self):
        print(self.possibles)
        for each in self.guessed:
            print(" ___",end='')
        print()
        for each in self.guessed:
            print("|", each, end=' ')
        print("|")
        for each in self.guessed:
            print(" ```", end='')
        print()

    def guessing(self):
        guess = ''
        while list(guess) != self.solution:
            guess = input(">")[:self.size].upper()
            for each in guess:
                print(each,end=":")
                if each in self.solution:
                    if guess.index(each) == self.solution.index(each):
                        print("          LOCKED")
                        self.guessed[guess.index(each)] = each
                    else:
                        print("          Exists")
                else:
                    print("----------------")
                    if each.upper() in self.possibles:
                        self.possibles.remove(each.upper())
            print('--------------------------------------------------------------------')
            self.print_current()


    def rolling(self):
        return chr(random.randint(65,90))

    def win(self):
        print()

if __name__ == '__main__':
    a = disarm()
    a.runcmd()
