#!/usr/bin/python3
""" CONSOLE """
import cmd
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """ HBNB command processor """
    prompt = "(hbnb) "
    list_of_existing_classes = [
        "BaseModel", "User", "State",
        "City", "Amenity", "Place",
        "Review"
        ]

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
        if validate_cmd(line, self.list_of_existing_classes) == 1:
            return
        p_line = shlex.split(line)
        key = p_line[0] + "." + p_line[1]
        if key not in models.storage.all().keys():
            print("** no instance found **")
            return
        else:
            print(models.storage.all().get(key))

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if validate_cmd(line, self.list_of_existing_classes) == 1:
            return
        p_line = shlex.split(line)
        key = p_line[0] + "." + p_line[1]
        if key not in models.storage.all().keys():
            print("** no instance found **")
            return
        else:
            models.storage.all().pop(key)
            models.storage.save()

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
                print(list_of_obj)
                return

        if line == "":
            for v in models.storage.all().values():
                list_of_obj.append(v.__str__())
            print(list_of_obj)
            return

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

    def help_count(self):
        """count command"""
        print("count the amount of instance for given class")

    def emptyline(self):
        """Over emptyline() method"""
        pass

    def count_n_of_instance(self, line):
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
                return len(list_of_obj)

    def default(self, line):
        """Default commands"""
        get_class = line.split(".")
        get_command = get_class[1].split("(")
        get_pre_args = get_command[-1].split(")")
        get_args = get_pre_args[0].split(", ")
        if get_class[0] in self.list_of_existing_classes:
            if get_command[0] == "all":
                self.do_all(get_class[0])
                return
            elif get_command[0] == "count":
                print(self.count_n_of_instance(get_class[0]))
                return
            elif get_command[0] == "show":
                self.do_show(get_class[0] + " " + get_args[0])
                return
            elif get_command[0] == "destroy":
                self.do_destroy(get_class[0] + " " + get_args[0])
                return
            elif get_command[0] == "update":
                self.do_update(
                    get_class[0] + " " + get_args[0] + " "
                    + get_args[1] + " " + get_args[2]
                    )
                return
        else:
            print("** class doesn't exist **")
            return


def validate_cmd(line, list_of_c):
    """Validates command to
    see if class exits...
    """
    p_line = shlex.split(line)
    if len(line) == 0:
        print("** class name missing **")
        return 1
    elif p_line[0] not in list_of_c:
        print("** class doesn't exist **")
        return 1
    elif len(p_line) < 2:
        print("** instance id missing **")
        return 1
    return 0


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
