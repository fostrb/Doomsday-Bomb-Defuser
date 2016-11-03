import os
class Program(object):
    def __init__(self, name, usage=None, brief=None, privileges="guest"):
        self.name = name
        self.privileges = privileges
        self.usage = usage or ''
        self.brief = brief or ''

banner = """
 ____                                          ______
|                        ..'''' `````|`````  .~      ~.
|______               .''            |      |          |
|                  ..'               |      |          |
|___________ ....''                  |       `.______.'
"""

initial = """Enter "help" for command list
"""

curUser = "guest"

armed = False

admins = {"root":"toor"}
promptSuffix = "@estoBombRig>"
prompt = curUser+promptSuffix

filesdir = "/home/ben/PycharmProjects/bombDefuser/FILESDIR"
fileslist = []
for each in os.listdir(filesdir):
    fileslist.append(each)

crypto1Locked = False
crypto2Locked = False

pullACard = """
------------------------------------------------------------
OOG: Pull a card from the "bad shit happens" deck.
------------------------------------------------------------
"""