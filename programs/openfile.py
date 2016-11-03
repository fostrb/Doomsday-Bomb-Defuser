from core import Program
import os
from os import listdir
from os.path import isfile, join
import core

class openfile(Program):
    def __init__(self, name="open", brief="Open a file. USAGE: \"open filename\""):
        super(openfile, self).__init__(name=name, brief=brief)
        self.alias = ["cat"]

    def runcmd(self, args):
        if not args or args[0] == "help":
            print(self.brief)
        else:
            self.filelist = [f for f in listdir(core.filesdir) if isfile(join(core.filesdir, f))]
            if args[0] in self.filelist:
                f = open(core.filesdir+'/'+args[0])
                line = f.readline()
                if 'LOCK' in f.readline():
                    print("LOCKED")
                    return
                os.system("cat "+core.filesdir+'/'+args[0])
                print()
            else:
                print("File not found")