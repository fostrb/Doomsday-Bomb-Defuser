from core import Program
from os import listdir
import core

class files(Program):
    def __init__(self, name="files", brief="Lists available files"):
        super(files, self).__init__(name=name, brief=brief)
        self.alias = ["ls", "dir", "l"]
        self.filelist = []

    def runcmd(self, args):
        for each in core.fileslist:
            print("\t",each)