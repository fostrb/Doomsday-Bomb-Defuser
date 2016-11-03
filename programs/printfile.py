from core import Command
import core
from os import listdir
from os.path import isfile, join

class printfile(Command):
    def __init__(self, name="print", brief="Physically print a file. USAGE: print filename", privileges="root"):
        super(printfile, self).__init__(name=name, brief=brief, privileges=privileges)
        self.alias = ["printfile"]


    def runcmd(self, args):
        if not args or args[0] == "help":
            print(self.brief)
        else:
            self.filesdir = self.filesdir = "/home/ben/PycharmProjects/bombDefuser/FILESDIR"
            self.filelist = [f for f in listdir(self.filesdir) if isfile(join(self.filesdir, f))]
            if args[0] in self.filelist:
                print("\n\tPrinting", args[0], "...\n")
            else:
                print("File not found")