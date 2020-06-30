#!/usr/bin/python3
""" CONSOLE """
import cmd
import json
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ HBNB command processor """
    prompt = "(hbnb) "
    list_of_existing_classes = ["BaseModel"]

    def do_EOF(self, line):
        """EOF command to exit the program\n"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel\n"""
        p_line = line.split()
        if len(line) == 0:
            print("** class name missing **")
        elif p_line[0] not in self.list_of_existing_classes:
            print("** class doesn't exist **")
        else:
            my_model = BaseModel()
            my_model.save()
            print(my_model.id)

    def do_show(self, line):
        """Prints the string representation of an instance\n"""
        stat = validate_cmd(line, self.list_of_existing_classes)
        if stat[0] is 0:
            p_line = stat[1]
            for v in models.storage.all().values():
                if v.__class__.__name__ == p_line[0] and v.id == p_line[1]:
                    print(v)
                    return
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id\n"""
        stat = validate_cmd(line, self.list_of_existing_classes)
        status = 1
        if stat[0] is 0:
            p_line = stat[1]
            for k, v in models.storage.all().items():
                if v.__class__.__name__ == p_line[0] and v.id == p_line[1]:
                    status = 0
                    key = k
            if status == 0:
                models.storage.all().pop(key)
                models.storage.save()
            if status == 1:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances\n"""
        p_line = line.split()
        list_of_obj = []
        if len(p_line) >= 1:
            if p_line[0] not in self.list_of_existing_classes:
                print("** class doesn't exist **")
            else:
                for v in models.storage.all().values():
                    if v.__class__.__name__ == p_line[0]:
                        list_of_obj.append(v.__str__())

        if line == "":
            for v in models.storage.all().values():
                list_of_obj.append(v.__str__())

        print(list_of_obj)

    def do_update(self, line):
        """Updates an instance based on the class name and id\n"""
        has_space = line.split('"')
        val = ""
        status = 1
        if len(has_space) > 1:
            val = has_space[1]
        p_line = line.split()
        if len(line) == 0:
            print("** class name missing **")
            return
        elif p_line[0] not in self.list_of_existing_classes:
            print("** class doesn't exist **")
            return
        elif len(p_line) < 2:
            print("** instance id missing **")
            return
        elif len(p_line) == 2:
            for v in models.storage.all().values():
                if v.__class__.__name__ == p_line[0] and v.id == p_line[1]:
                    status = 0
                if status == 1:
                    print("** no instance found **")
                    return
        if len(p_line) < 3:
            print("** attribute name missing **")
            return
        elif len(p_line) < 4:
            print("** value missing **")
            return
        else:
            for v in models.storage.all().values():
                if len(has_space) == 1:
                    val = p_line[3]
                if v.__class__.__name__ == p_line[0] and v.id == p_line[1]:
                    v.__dict__.update({p_line[2]: val})
                    models.storage.save()

    def emptyline(self):
        """Over emptyline()
        method
        """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')


def validate_cmd(line, list_of_c):
    """Validates command to
    see if class exits...
    """
    state = 0
    p_line = line.split()
    if len(line) == 0:
        print("** class name missing **")
        state = 1
    elif p_line[0] not in list_of_c:
        print("** class doesn't exist **")
        state = 1
    elif len(p_line) < 2:
        print("** instance id missing **")
        state = 1

    return (state, p_line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
