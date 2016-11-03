from core import Command
import core
from time import sleep

class unlock(Command):
    def __init__(self, name="unlock", brief="Bomb unlock utility", privileges="root"):
        super(unlock, self).__init__(name=name, brief=brief, privileges=privileges)
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
        if not core.armed:
            print("Bomb is not armed.")
            return
        print("disarming")
        if core.crypto1Locked:
            print("CryptoLock 1:")
            for each in core.crypto1Locked:
                print(self.morse[each.upper()], end=' ', flush=True)
                sleep(.5)
            print()
            guess = ""
            attempts = 0
            while guess.upper()!= core.crypto1Locked.upper():
                if attempts >=1:
                    print("INCORRECT DECODING")
                if attempts == 3:
                    print(core.pullACard)
                    return
                guess = input("Input decoded lock:")
                attempts+=1
            core.crypto1Locked = False
            print("CryptoLock 1 Unlocked.")

        if core.crypto2Locked:
            print("CryptoLock 2:")
            for each in core.crypto2Locked:
                print(self.morse[each.upper()], end=' ', flush=True)
                sleep(.5)
            print()
            guess = ""
            attempts = 0
            while guess.upper()!= core.crypto2Locked.upper():
                if attempts >=1:
                    print("INCORRECT DECODING")
                if attempts == 3:
                    print(core.pullACard)
                    return
                guess = input("Input decoded lock:")
                attempts+=1
            core.crypto2Locked = False
            print("CryptoLock 2 Unlocked.")