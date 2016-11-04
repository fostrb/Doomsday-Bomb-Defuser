from core import Program
from time import sleep
import estoBomb

class armBomb(Program):
    def __init__(self, name="armBomb", brief="Arms the bomb and dumps bomb connection", programType="ESTO Bomb Utilities"):
        super(armBomb, self).__init__(name=name, brief=brief, programType=programType)
        self.alias = ["arm"]

    def runcmd(self, args):
        if estoBomb.armed==False:
            estoBomb.armed=True
            print("ARMING BOMB:")
            sleep(1)
            print("CHECKING HARDWARE", end='', flush=True)
            self.loadingBar()
            print("FLIPPING SWITCHES", end='', flush=True)
            self.loadingBar()
            print("ROLLING CRYPTO LOCKS", end='', flush=True)
            estoBomb.crypto_lock1 = 'deadbeef'
            estoBomb.crypto_lock2 = 'password'
            self.loadingBar()
            print("Bomb armed. Get the fuck out of there.")
        else:
            print("Bomb is already armed.")

    def loadingBar(self):
        for i in range(1,10):
            print(".", end='', flush=True)
            sleep(.1)
        print(".")