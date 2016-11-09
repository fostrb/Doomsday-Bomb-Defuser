from core import Program
from time import sleep
import core
import os
class connect(Program):
    def __init__(self, name="connect", brief="Connect to a hard-wired device"):
        super(connect, self).__init__(name=name, brief=brief)
        self.alias = ["connect"]

    def runcmd(self, args):
        if args:
            if args[0] == "help":
                print(self.brief)
                print("Hard-wire cyberdeck to a device.")
                print("This utility will auto-detect device and allow interfacing.")
        else:
            if core.connected_to_bomb:
                print("Already connected to ESTO BOMB.")
                return
            print("Connecting to hard-wired device", end='')
            self.loadingBar()
            print("Fingerprinting device" ,end='')
            self.loadingBar()
            print("ESTO BOMB detected")
            sleep(2)
            print("\t-Dual cryptographic locks detected")
            sleep(2)
            print("\t-Arming utility detected")
            sleep(2)
            print("\t-Payload detected")
            self.loadingBar()
            print("ESTO BOMB is connected.")
            print("ESTO BOMB is ready to be interfaced with.")
            core.connected_to_bomb = True


    def loadingBar(self):
        for i in range(1,10):
            print(".", end='', flush=True)
            sleep(.1)
        print(".")