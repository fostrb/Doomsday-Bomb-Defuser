from core import Program
import core

class bombStatus(Program):
    def __init__(self, name="bombStatus", brief="Check bomb status"):
        super(bombStatus, self).__init__(name=name, brief=brief)
        self.alias = ["status"]

    def runcmd(self, args):
        print("BOMB:", end='')
        if core.armed:
            print("\t\tARMED")
        else:
            print("\t\tNOT ARMED")
        print("crypto1:", end='')
        if core.crypto1Locked:
            print("\tLOCKED")
        else:
            print("\tUNLOCKED")
        print("crypto2:", end='')
        if core.crypto2Locked:
            print("\tLOCKED")
        else:
            print("\tUNLOCKED")