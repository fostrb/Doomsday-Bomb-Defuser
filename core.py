import os
from os import listdir
from os.path import isfile, join

class Program(object):
    def __init__(self, name, usage=None, brief=None, privileges="guest", programType="Basic Utilities"):
        self.name = name
        self.privileges = privileges
        self.usage = usage or ''
        self.brief = brief or ''
        self.programType = programType

class CyberDeck(object):
    def __init__(self, name, rank=1):
        self.name=name
        self.rank=rank


connected_to_bomb = False

banner = """
 ____                                          ______
|                        ..'''' `````|`````  .~      ~.
|______               .''            |      |          |
|                  ..'               |      |          |
|___________ ....''                  |       `.______.'
                                --Bomb Rig Deck---
"""
filesdir = os.path.normpath("./FILESDIR")

def load_programs():
    from programs import files, openfile, clear, whoami, printfile, unlock, armBomb, bombStatus, disarm, vampyre, cryolock, connect
    return [files.files(), openfile.openfile(), clear.clear(), whoami.whoami(), printfile.printfile(), unlock.unlock(), armBomb.armBomb(), bombStatus.bombStatus(), disarm.disarm(), vampyre.vampyre(), cryolock.cryolock(), connect.connect()]

def get_files():
    fileslist = [f for f in listdir(filesdir) if isfile(join(filesdir, f))]
    return fileslist

def is_locked(file):
    f = open(os.path.normpath(filesdir+'/'+file))
    line = f.readline()
    if("!!" in line):
        return line.split(':')
    else:
        return False

programs=load_programs()

initial = """Enter "help" for command list
"""


promptSuffix = "estoBombDeck>"
prompt = promptSuffix

pullACard = """
------------------------------------------------------------
OOG: Pull a card from the "bad shit happens" deck.
------------------------------------------------------------
"""