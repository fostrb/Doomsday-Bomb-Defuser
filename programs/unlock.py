from core import Program
import core
from time import sleep
import estoBomb

class unlock(Program):
    def __init__(self, name="unlock", brief="Unlock bomb crypto locks", privileges="root", programType="ESTO Bomb Utilities"):
        super(unlock, self).__init__(name=name, brief=brief, privileges=privileges, programType=programType)
        self.alias = ["unlock"]
        self.morse = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

    def runcmd(self, args):
        if not estoBomb.armed:
            print("Bomb is not armed.")
            return
        print("disarming")
        if estoBomb.crypto_lock1:
            print("CryptoLock 1:")
            for each in estoBomb.crypto_lock1:
                print(self.morse[each.upper()], end=' ', flush=True)
                sleep(.5)
            print()
            guess = ""
            attempts = 0
            while guess.upper()!= estoBomb.crypto_lock1.upper():
                if attempts >=1:
                    print("INCORRECT DECODING")
                if attempts == 3:
                    print(core.pullACard)
                    return
                guess = input("Input decoded lock:")
                attempts+=1
            estoBomb.crypto_lock1 = False
            print("CryptoLock 1 Unlocked.")

        if estoBomb.crypto_lock2:
            print("CryptoLock 2:")
            for each in estoBomb.crypto_lock2:
                print(self.morse[each.upper()], end=' ', flush=True)
                sleep(.5)
            print()
            guess = ""
            attempts = 0
            while guess.upper()!= estoBomb.crypto_lock2.upper():
                if attempts >=1:
                    print("INCORRECT DECODING")
                if attempts == 3:
                    print(core.pullACard)
                    return
                guess = input("Input decoded lock:")
                attempts+=1
            estoBomb.crypto_lock2= False
            print("CryptoLock 2 Unlocked.")