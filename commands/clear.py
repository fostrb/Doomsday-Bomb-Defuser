from core import Command
import core
import os

class clear(Command):
    def __init__(self, name="clear", brief="clear screen"):
        super(clear, self).__init__(name=name, brief=brief)
        self.alias = ["cls"]

    def runcmd(self, args):
        os.system('cls' if os.name =='nt' else 'clear')
        print(core.banner)
        print(core.initial)