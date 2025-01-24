#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command line interpreter for the AirBnB clone."""
    
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exits the program."""
        return True

    def do_EOF(self, arg):
        """Exits the program when EOF is entered."""
        return True

    def do_create(self, class_name):
        """Creates a new instance of BaseModel, saves it and prints the id."""
        if not class_name:
            print("** class name missing **")
        elif class_name != 'BaseModel':
            print("** class doesn't exist **")
        else:
            instance = BaseModel()
            storage.new(instance)
            storage.save()
            print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name, instance_id = args
        if class_name != 'BaseModel':
            print("** class doesn't exist **")
            return
        key = f"BaseModel.{instance_id}"
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name, instance_id = args
        if class_name != 'BaseModel':
            print("** class doesn't exist **")
            return
        key = f"BaseModel.{instance_id}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances."""
        if arg and arg != 'BaseModel':
            print("** class doesn't exist **")
        else:
            instances = [str(instance) for instance in storage.all().values()]
            print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        class_name, instance_id, attribute_name, attribute_value = args
        if class_name != 'BaseModel':
            print("** class doesn't exist **")
            return
        key = f"BaseModel.{instance_id}"
        if key in storage.all():
            instance = storage.all()[key]
            setattr(instance, attribute_name, attribute_value)
            instance.save()
        else:
            print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()

