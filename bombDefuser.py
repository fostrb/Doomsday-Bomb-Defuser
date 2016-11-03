import os
import core
import signal

'''
TODO:
-bombUnlock
-bomb defusal file
'''

class bombDefuser(object):
        def __init__(self):
            os.system('cls' if os.name =='nt' else 'clear')
            print(core.banner)
            print(core.initial)
            self.cmds = self.load_cmds()
            signal.signal(signal.SIGINT, self.sigint_handler)
            signal.signal(signal.SIGTSTP, self.sigtstp_handler)


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
            for loaded in self.cmds:
                if command == loaded.name:
                    if core.curUser == "guest":
                        if loaded.privileges != "guest":
                            print("gotta have ROOT to do that, sucka")
                            return
                    loaded.runcmd(cmd_args)
                    return
                if command in loaded.alias:
                    loaded.runcmd(cmd_args)
                    return
            if command == "logout":
                os.system('cls' if os.name =='nt' else 'clear')
                self.login_screen()
            elif command in ["cmds","programs", "help"]:
                for each in self.cmds:
                    print("\t",each.name, ":", each.brief)
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


        def load_cmds(self):
            from programs import files, openfile, clear, whoami, printfile, unlock, armBomb, bombStatus, disarm, vampyre
            return [files.files(), openfile.openfile(), clear.clear(), whoami.whoami(), printfile.printfile(), unlock.unlock(), armBomb.armBomb(), bombStatus.bombStatus(), disarm.disarm(), vampyre.vampyre()]


if __name__ == "__main__":
    a = bombDefuser()
    a.main_loop()