#!/usr/bin/python3
""" CONSOLE """
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ HBNB command processor """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF command to exit the program\n"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Over emptyline()
        method
        """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
