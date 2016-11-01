from core import Command
from os import listdir
import core

class files(Command):
    def __init__(self, name="files", brief="Lists available files"):
        super(files, self).__init__(name=name, brief=brief)
        self.alias = ["ls", "dir", "l"]
        self.filelist = []

    def runcmd(self, args):
        self.filesdir = self.filesdir = "/home/ben/PycharmProjects/bombDefuser/FILESDIR"

        for each in listdir(self.filesdir):
            self.filelist.append(each)
            print("\t",each)