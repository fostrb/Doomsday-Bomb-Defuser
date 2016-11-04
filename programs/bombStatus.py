from core import Program
import core
import estoBomb

class bombStatus(Program):
    def __init__(self, name="bombStatus", brief="Check bomb status", programType="ESTO Bomb Utilities"):
        super(bombStatus, self).__init__(name=name, brief=brief, programType=programType)
        self.alias = ["status"]

    def runcmd(self, args):
        print("BOMB:", end='')
        if estoBomb.armed:
            print("\t\tARMED")
        else:
            print("\t\tNOT ARMED")
        print("crypto1:", end='')
        if estoBomb.crypto_lock1:
            print("\tLOCKED")
        else:
            print("\tUNLOCKED")
        print("crypto2:", end='')
        if estoBomb.crypto_lock2:
            print("\tLOCKED")
        else:
            print("\tUNLOCKED")