from core import Program
import core

class files(Program):
    def __init__(self, name="files", brief="Lists available files"):
        super(files, self).__init__(name=name, brief=brief)
        self.alias = ["ls", "dir", "l"]
        self.filelist = []

    def runcmd(self, args):
        for each in core.get_files():
            print("\t",each.ljust(40), end='')
            if core.is_locked(each):
                print("LOCKED")
            else: print("")