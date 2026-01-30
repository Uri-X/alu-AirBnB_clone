#!/usr/bin/python3
"""
Module for console
"""
import cmd
import re
import shlex
import ast
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


def split_curly_braces(e_arg):
    """
    Splits the curly braces for the update method
    """
    curly_braces = re.search(r"\{(.*?)\}", e_arg)
    if curly_braces:
        id_with_comma = shlex.split(e_arg[:curly_braces.span()[0]])
        id_ = [i.strip(",") for i in id_with_comma][0]
        str_data = curly_braces.group(1)
        try:
            arg_dict = ast.literal_eval("{" + str_data + "}")
        except Exception:
            print("** invalid dictionary format **")
            return None, None
        return id_, arg_dict
    else:
        commands = e_arg.split(",")
        if commands:
            try:
                id_ = commands[0].strip()
            except Exception:
                return "", ""
            try:
                attr_name = commands[1].strip()
            except Exception:
                return id_, ""
            try:
                attr_value = commands[2].strip()
            except Exception:
                return id_, attr_name
            return id_, f"{attr_name} {attr_value}"
        return "", ""


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "Amenity", "Place", "Review", "State", "City"]
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
        "State": State,
        "City": City
    }

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_EOF(self, arg):
        """
        EOF (Ctrl+D) signal to exit the program.
        """
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_create(self, arg):
        """
        Create a new instance of a class and save it to the JSON file.
        Usage: create <class_name>
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
            return
        class_name = commands[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        new_instance = self.__classes[class_name]()
        storage.new(new_instance)
        storage.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Shows the string representation of an instance.
        Usage: show <class_name> <id>
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        Usage: destroy <class_name> <id>
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Print the string representation of all instances or a specific class.
        """
        objects = storage.all()
        commands = shlex.split(arg)
        if len(commands) == 0:
            for value in objects.values():
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def do_count(self, arg):
        """
        Counts the number of instances of a class
        usage: <class name>.count()
        """
        objects = storage.all()
        commands = shlex.split(arg)
        if not arg:
            print("** class name missing **")
            return
        cls_nm = commands[0]
        if cls_nm not in self.valid_classes:
            print("** class doesn't exist **")
            return
        count = sum(1 for obj in objects.values() if obj.__class__.__name__ == cls_nm)
        print(count)

    def do_update(self, arg):
        """
        Update an instance by adding or updating an attribute.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
               or update <class_name> <id> {dict}
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        obj_id = args[1]
        key = f"{class_name}.{obj_id}"
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return

        obj = objects[key]

        # Dictionary update
        curly_braces = re.search(r"\{(.*?)\}", arg)
        if curly_braces:
            try:
                str_data = curly_braces.group(1)
                arg_dict = ast.literal_eval("{" + str_data + "}")
                for attr_name, attr_value in arg_dict.items():
                    setattr(obj, attr_name, attr_value)
            except Exception:
                print("** invalid dictionary format **")
                return
        else:
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attr_name = args[2]
            attr_value = args[3]
            try:
                attr_value = eval(attr_value)
            except:
                pass
            setattr(obj, attr_name, attr_value)

        obj.save()

    def default(self, arg):
        """Handle <class>.<command>(args) syntax more robustly"""
        arg = arg.strip()
        if '.' not in arg or '(' not in arg or ')' not in arg:
            print("*** Unknown syntax: {}".format(arg))
            return False

        try:
            # Split class from rest
            class_name, rest = arg.split('.', 1)
            class_name = class_name.strip()

            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
                return False

            # Get command and args string
            cmd_part, args_part = rest.split('(', 1)
            cmd = cmd_part.strip()
            args_part = args_part.rstrip(')').strip()

            # Map to methods
            method_map = {
                'all': self.do_all,
                'count': self.do_count,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update
            }

            if cmd not in method_map:
                print("*** Unknown syntax: {}".format(arg))
                return False

            # Prepare argument string for space notation
            cmd_arg = class_name
            if args_part:
                # Remove outer quotes if the whole args is quoted
                if args_part.startswith('"') and args_part.endswith('"'):
                    args_part = args_part[1:-1].strip()
                cmd_arg += " " + args_part

            # Call the method
            method_map[cmd](cmd_arg)
            return False

        except Exception:
            print("*** Unknown syntax: {}".format(arg))
            return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()