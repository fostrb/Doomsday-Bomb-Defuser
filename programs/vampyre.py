from core import Program
import core
import random
from os.path import isfile, join
import os
from time import sleep

class vampyre(Program):
    def __init__(self, name="vampyre", brief="Cyber lockpick utility", privileges="guest"):
        super(vampyre, self).__init__(name=name, brief=brief, privileges=privileges)
        self.alias = ["vamp"]

    def runcmd(self, args):
        self.print_vamPYre()
        print("ARGS:",args)
        if not args:
            print("Enter a target to unlock.")
            return
        if (args[0].lower() == '--sweep')or args[0].lower() == '-s':
            print("sweeping...")
            filelist = [f for f in os.listdir(core.filesdir) if isfile(join(core.filesdir, f))]
            for file in filelist:
                print('\t',file,end='', flush=True)
                self.loadingBar()
                if self.checkVulnerable(file):
                    print("\t\t\tVULNERABLE")
                else:
                    print("")
            return
        elif args[0] not in core.fileslist:
            print("NOPE")
            return
        else:
            num = self.checkVulnerable(args[0])
            if num:
                print("NUMBER:", num)
                self.disarming_utility(int(num))



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

        vampyreAlternate="""
               ____________________
        __    /
          \  / AMPIRE
           \/

        """
        #os.system("clear")
        #print(vamPYre)
        print(vampyreAlternate)

    def loadingBar(self):
        for i in range(1,10):
            print(".", end='', flush=True)
            sleep(.1)

    def checkVulnerable(self, file):
        f = open(core.filesdir+'/'+file)
        line = f.readline()
        if("VAMPLOCK" in line):
            return line.split(':')[1]


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
    a = vampyre()
    a.runcmd()
