from core import Command
import core
from time import sleep
import os

class armBomb(Command):
    def __init__(self, name="armBomb", brief="Bomb arming utility"):
        super(armBomb, self).__init__(name=name, brief=brief)
        self.alias = ["arm"]

    def runcmd(self, args):
        if core.armed==False:
            core.armed=True
            print("ARMING BOMB:")
            sleep(1)
            print("CHECKING HARDWARE", end='', flush=True)
            self.loadingBar()
            print("FLIPPING SWITCHES", end='', flush=True)
            self.loadingBar()
            print("ROLLING CRYPTO LOCKS", end='', flush=True)
            core.crypto1Locked = "DEADBEEF"
            core.crypto2Locked = "password"
            self.loadingBar()
            print("Bomb armed. Get the fuck out of there.")
        else:
            print("Bomb is already armed.")

    def loadingBar(self):
        for i in range(1,10):
            print(".", end='', flush=True)
            sleep(.1)
        print(".")