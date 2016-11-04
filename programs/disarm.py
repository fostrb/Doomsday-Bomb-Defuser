from core import Program
import core
import estoBomb
import random
import os
from time import sleep

class disarm(Program):
    def __init__(self, name="disarm", brief="Bomb disarming utility", privileges="root", programType="ESTO Bomb Utilities"):
        super(disarm, self).__init__(name=name, brief=brief, privileges=privileges, programType=programType)
        self.alias = ["disarm"]

    def runcmd(self, args):
        if not estoBomb.armed:
            print("Bomb is not currently armed.")
            return
        if estoBomb.crypto_lock1 or estoBomb.crypto_lock2:
            print("Both crypto locks must be unlocked")
            print("Crypto1Lock:", estoBomb.crypto_lock1)
            print("Crypto2Lock:", estoBomb.crypto_lock2)
            return
        self.disarming_utility()


    def disarming_utility(self):
        print("DISARMING BOMB...")
        estoBomb.armed = False
