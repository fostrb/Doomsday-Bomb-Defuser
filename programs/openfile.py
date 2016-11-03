from core import Command
import os
from os import listdir
from os.path import isfile, join
import core

class openfile(Command):
    def __init__(self, name="open", brief="Open a file. USAGE: \"open filename\""):
        super(openfile, self).__init__(name=name, brief=brief)
        self.alias = ["cat"]

    def runcmd(self, args):
        if not args or args[0] == "help":
            print(self.brief)
        else:
            self.filesdir = self.filesdir = "/home/ben/PycharmProjects/bombDefuser/FILESDIR"
            self.filelist = [f for f in listdir(self.filesdir) if isfile(join(self.filesdir, f))]
            if args[0] in self.filelist:
                os.system("cat "+self.filesdir+'/'+args[0])
            else:
                print("File not found")