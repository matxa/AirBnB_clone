#!/usr/bin/python3
""" CONSOLE """
import cmd
import json
import models
from models.base_model import BaseModel
import shlex


class HBNBCommand(cmd.Cmd):
    """ HBNB command processor """
    prompt = "(hbnb) "
    list_of_existing_classes = ["BaseModel"]

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        p_line = line.split()
        if len(line) == 0:
            print("** class name missing **")
        elif p_line[0] not in self.list_of_existing_classes:
            print("** class doesn't exist **")
        else:
            eval_class = p_line[0] + "()"
            my_model = eval(eval_class)
            my_model.save()
            print(my_model.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        stat = validate_cmd(line, self.list_of_existing_classes)
        if stat[0] is 0:
            p_line = stat[1]
            for v in models.storage.all().values():
                if v.__class__.__name__ == p_line[0] and v.id == p_line[1]:
                    print(v)
                    return
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
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
        """Prints all string representation of all instances"""
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
        """Updates an instance based on the class name and id"""
        p_line = shlex.split(line)
        if len(line) == 0:
            print("** class name missing **")
            return
        elif p_line[0] not in self.list_of_existing_classes:
            print("** class doesn't exist **")
            return
        elif len(p_line) < 2:
            print("** instance id missing **")
            return
        key = p_line[0] + "." + p_line[1]
        if key not in models.storage.all().keys():
            print("** no instance found **")
            return
        elif len(p_line) < 3:
            print("** attribute name missing **")
            return
        elif len(p_line) < 4:
            print("** value missing **")
            return
        else:
            for v in models.storage.all().values():
                if v.__class__.__name__ == p_line[0] and v.id == p_line[1]:
                    if p_line[2] in v.__dict__.keys():
                        if type(v.__dict__.get(p_line[2])) == int:
                            if conv_int(p_line[3]):
                                p_line[3] = int(p_line[3])
                        elif type(v.__dict__.get(p_line[2])) == float:
                            if conv_float(p_line[3]):
                                p_line[3] = float(p_line[3])
                    v.__dict__.update({p_line[2]: p_line[3]})
                    v.save()

    def emptyline(self):
        """Over emptyline() method"""
        pass


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


def conv_int(var):
    """is var convertable to int"""
    try:
        int(var)
        return True
    except ValueError:
        return False


def conv_float(var):
    """is var convertable to float"""
    try:
        float(var)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
