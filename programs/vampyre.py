from core import Program
import core
import random
from os.path import isfile, join
import os
from time import sleep

class vampyre(Program):
    def __init__(self, name="vampyre", brief="Cyber lockpicking utility", privileges="guest", programType="Hacking Utilities"):
        super(vampyre, self).__init__(name=name, brief=brief, privileges=privileges, programType=programType)
        self.alias = ["vamp"]

    def runcmd(self, args):
        self.print_vamPYre()
        if not args:
            print("\nEnter a target to unlock.")
            print("USAGE: vampyre <locked file>")
            return
        if (args[0].lower() == 'help'):
          print("--vampyre cyber lockpicking utility")
          print("options:")
          print("\tSWEEP: --sweep (-s)")
          print("\t\t'vampyre --sweep'")
          print("\t\tSearch files for vulnerabilities. Files able to be unlocked will display as 'vulnerable'\n")
          print("\tLOCK: --lock (-l)")
          print("\t\t'vampyre --lock 5 <filename>'")
          print("\t\tLock a file, specifying complexity of lock.")
        elif (args[0].lower() == '--sweep')or args[0].lower() == '-s':
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
        elif (args[0].lower() == '--lock') or (args[0].lower() == '-l'):
            if args[1]:
                try:
                    complexity = int(args[1])
                except:
                    print("Invalid syntax")
                    print("Example: 'vampyre --lock 5 <file>")
                    return
                if 14 > complexity >1:
                    if args[2]:
                        if args[2] in core.get_files():
                            if core.is_locked(args[2]):
                                print(args[2], "is already locked.")
                                return
                            else:
                                inputString = "Locking", args[2], "with vampyre at complexity", complexity,": continue? (y/n)"
                                if input(inputString) in ["y", "yes", "Y", "YES"]:
                                    self.lock_waiting(complexity)
                                    f = open(os.path.normpath(core.filesdir+"/"+args[2]), "r")
                                    data = f.read()
                                    f.close()
                                    f = open(os.path.normpath(core.filesdir+"/"+args[2]), "w")
                                    f.write("!!:vampyre:"+str(complexity)+"\n")
                                    f.write(data)
                                    f.close()

            else:
                print("Enter the level of complexity that you would like to lock the file at. (1 - 13)")
                print("Higher levels of complexity will take exponentially longer to complete encryption.")
                print("Example: 'vampyre --lock 5 <file>")
        elif args[0] not in core.get_files():
            print("File doesn't exist")
            return
        else:
            lock = core.is_locked(args[0])
            if lock:
                if lock[1] == "vampyre":
                    num = core.is_locked(args[0])[2]
                    if num:
                        self.unlock(args[0], int(num))
                else:
                    print(args[0], "is not locked with vampyre.")
            else:
                print(args[0], "is unlocked.")

    def lock_waiting(self, complexity):
        for i in range(1, (complexity)*10):
            print(".",end='', flush=True)
            sleep(.5)
        print(".")


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
        print()

    def loadingBar(self):
        for i in range(1,10):
            print(".", end='', flush=True)
            sleep(.1)

    def unlock(self, file, size):
        self.size = size
        self.solution = []
        self.possibles = []
        self.roll_solution()
        self.guessed = ["-"]*self.size
        self.print_current()
        solved = self.guessing()
        if solved:
            f = open(os.path.normpath(core.filesdir+"/"+file), 'r')
            data = f.readlines()
            f.close()
            f = open(os.path.normpath(core.filesdir+"/"+file), 'w')
            for line in data:
                if "!!" not in line:
                    print(line)
                    f.write(line)
            f.truncate()
            f.close()
            print(file, "UNLOCKED")


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
        return True


    def rolling(self):
        return chr(random.randint(65,90))

    def win(self):
        print()