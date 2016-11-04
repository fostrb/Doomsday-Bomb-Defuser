import os
import core
import signal

'''
TODO:
-transfer bomb status things from CORE to ESTOBOMB
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
                    #if core.curUser == "guest":
                    #   if loaded.privileges != "guest":
                    #       print("gotta have ROOT to do that, sucka")
                    #        return
                    loaded.runcmd(cmd_args)
                    return
                if command in loaded.alias:
                    loaded.runcmd(cmd_args)
                    return
            if command == "logout":
                os.system('cls' if os.name =='nt' else 'clear')
                self.login_screen()
            elif command in ["cmds","programs", "help"]:
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
                print("\t","logout : return to login screen")
                print("\t","help : displays list of programs and their usages")
                return
            elif command == "stopthismadness":
                exit()
            else:
                print("Command not recognized. Enter \'help\' for a list of programs.")


        def login_screen(self):
            core.curUser = "guest"
            core.prompt = core.curUser+core.promptSuffix
            print(core.banner)
            print("Please enter your username and password")
            uname = ""
            while uname not in core.admins:
                uname = input("USERNAME:") or "guest"
                if uname == "guest":
                    return
                if uname in core.admins:
                    password = input("PASSWORD:")
                    if password == core.admins[uname]:
                        core.curUser = uname
                        core.prompt = core.curUser+core.promptSuffix
                        print("LOGGED IN AS", core.curUser.upper())
                    else:
                        os.system('cls' if os.name =='nt' else 'clear')
                        print("PASSWORD INCORRECT")
                        self.login_screen()
                else:
                    os.system('cls' if os.name =='nt' else 'clear')
                    print(core.banner)
                    print("USER NOT FOUND")

if __name__ == "__main__":
    a = DeckTerminal()
    a.main_loop()