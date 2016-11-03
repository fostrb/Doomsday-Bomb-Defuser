from core import Program
import core
import random
from os.path import isfile, join
import os
from time import sleep

class vampyre(Program):
    def __init__(self, name="vampyre", brief="Cyber lockpick utility", privileges="guest", programType="Hacking Utilities"):
        super(vampyre, self).__init__(name=name, brief=brief, privileges=privileges, programType=programType)
        self.alias = ["vamp"]

    def runcmd(self, args):
        self.print_vamPYre()
        if not args:
            print("\nEnter a target to unlock.")
            print("USAGE: vampyre <locked file>")
            return
        if (args[0].lower() == '--sweep')or args[0].lower() == '-s':
            print("sweeping...")
            filelist = [f for f in os.listdir(core.filesdir) if isfile(join(core.filesdir, f))]
            for file in filelist:
                print('\t',file.ljust(40),end='', flush=True)
                self.loadingBar()
                lock = core.is_locked(file)
                if lock:
                    if lock[1] == "vampyre":
                        print("---VULNERABLE---")
                    else:
                        print("LOCKED")
                else:
                    print("UNLOCKED")
            return
        elif args[0] not in core.get_files():
            print("NOPE")
            return
        else:
            num = core.is_locked(args[0])[2]
            if num:
                self.disarming_utility(int(num))



    def print_vamPYre(self, clear=False):
        vampyre="""
               ____________________
     ___      /     _________
        \    / AMP\/RE
         \  /     / cyber lockpicking utility
          \/    \/
        """
        if clear:
            os.system("clear")
        for each in vampyre:
            print(each,end='',flush=True)
            sleep(.008)

    def loadingBar(self):
        for i in range(1,10):
            print(".", end='', flush=True)
            sleep(.1)

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
            if '!' in guess:
                print("Leaving vampyre")
                return
            for each in guess:
                print(each,end=":")
                if each in self.solution:
                    if guess.index(each) == self.solution.index(each):
                        print("LOCKED".rjust(20))
                        self.guessed[guess.index(each)] = each
                    else:
                        print("Exists".rjust(20))
                else:
                    print("--------------------")
                    if each.upper() in self.possibles:
                        self.possibles.remove(each.upper())
            print('--------------------------------------------------------------------')
            self.print_current()


    def rolling(self):
        return chr(random.randint(65,90))

    def win(self):
        print()

if __name__ == '__main__':
    a = vampyre()
    a.runcmd()