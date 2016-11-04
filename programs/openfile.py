from core import Program
import core
import os
class openfile(Program):
    def __init__(self, name="open", brief="Open a file. USAGE: \"open filename\""):
        super(openfile, self).__init__(name=name, brief=brief)
        self.alias = ["cat"]

    def runcmd(self, args):
        if not args or args[0] == "help":
            print(self.brief)
        else:
            self.filelist = core.get_files()
            if args[0] in self.filelist:
                lock = core.is_locked(args[0])
                if lock:
                    print("\tFile", args[0], "is", lock[1], "LOCKED.")
                    if lock[1] in core.programs:
                        print("\tTry using ", lock[1], "to unlock the file.")
                        print("\tExample: \"", lock[1], args[0], "\" ")
                    else:
                        print(lock[1], "is not installed on this deck.")
                    return
                f = open(os.path.normpath(core.filesdir+'/'+args[0]))
                contents = f.read()
                print(contents)
                print()
            else:
                print("File not found")