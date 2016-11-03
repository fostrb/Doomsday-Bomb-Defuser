from core import Program
import core

class whoami(Program):
    def __init__(self, name="whoami", brief="Echos the current user and their privileges"):
        super(whoami, self).__init__(name=name, brief=brief)
        self.alias = ["user"]

    def runcmd(self, args):
        privs = ""
        print(core.curUser, end ='\t')
        if core.curUser == "guest":
            privs = "basic"
        elif core.curUser == "root":
            privs = "administrative"
        elif core.curUser == "summersv":
            privs = "Top Secret/SCI"
        print("privileges:", privs)