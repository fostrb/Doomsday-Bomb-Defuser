import os
import core
import signal

'''
TODO:
-write a bomb connection program
-while not connected to bomb, unload bomb-specific programs
-bombUnlock
-bomb Disarm
-bomb defusal file

-fix cat program "X is not installed on this deck"
'''

class DeckTerminal(object):
        def __init__(self):
            os.system('cls' if os.name =='nt' else 'clear')
            print(core.banner)
            print(core.initial)
            signal.signal(signal.SIGINT, self.sigint_handler)
            #signal.signal(signal.SIGTSTP, self.sigtstp_handler)

        def sigtstp_handler(self, signum, frame):
            print()
            print("\n",core.prompt,end='')


        def sigint_handler(self, signum, frame):
            print()
            print("\n",core.prompt,end='')


        def main_loop(self):
            while True:
                self.parse_cmd(self.get_cmd())


        def get_cmd(self):
            while True:
                try:
                    return input(core.prompt)
                except:
                    continue


        def parse_cmd(self, cmd):
            if cmd=="":
                return
            sep = cmd.split()
            command = sep.pop(0)
            cmd_args = sep
            for loaded in core.programs:
                if command == loaded.name:
                    loaded.runcmd(cmd_args)
                    return
                if command in loaded.alias:
                    loaded.runcmd(cmd_args)
                    return
            if command in ["cmds","programs", "help"]:
                progDict = {}
                for each in core.programs:
                    if each.programType not in progDict.keys():
                        progDict[each.programType]=[]
                    progDict[each.programType].append(each)
                for progType in progDict.keys():
                    print("---",progType, "--------------------")
                    for program in progDict[progType]:
                        print("\t",program.name,":",program.brief)
                print("---System Specific------------------")
                print("\t","help : displays list of programs and their usages")
                return
            elif command == "stopthismadness":
                exit()
            else:
                print("Command not recognized. Enter \'help\' for a list of programs.")


if __name__ == "__main__":
    a = DeckTerminal()
    a.main_loop()