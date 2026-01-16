<<<<<<< HEAD
![image](https://github.com/user-attachments/assets/a7a7225e-4293-4c7c-b206-fa15c2af0057)

<h1>AIRBNB CLONE Project</h1>

### This project involves creating a basic clone of the AirBnB website, focusing initially on a backend console to manage data, similar to a shell interface. The console commands will enable users to create, update, and delete objects, as well as manage file storage.

### Console Tasks:
- Implement a parent class named `BaseModel` for handling initialization, serialization, and deserialization of instances.
- Establish a straightforward flow for serialization and deserialization: Instance <-> Dictionary <-> JSON string <-> file.
- Develop all necessary classes for AirBnB (such as User, State, City, Place, etc.) that derive from `BaseModel`.
- Create the project's first abstracted storage engine: File storage.
- Write unit tests to validate all classes and the storage engine.

### Command Interpreter Description:
The command interpreter facilitates the management of project objects by enabling:

- Creation of new objects (e.g., a new User or Place).
- Retrieval of objects from files, databases, etc.
- Performing operations on objects (like counting or computing statistics).
- Updating object attributes.
- Deleting objects.

- ### Starting the Interpreter
- To start the interpreter, run the `console.py` file. Once the interpreter is active, you will see the prompt `(hbnb)`.

### Basic Commands:
- **help**: Displays a list of available commands.
  
  Example usage:
  ```
  (hbnb) help
  ```

  This will show documented commands:
  ```
  Documented commands (type help <topic>):
  ========================================
  EOF  all  create  delete  destroy  exit  help  q  quit  show  update
  ```

- **quit** or **exit**: Ends the console session.

  Example usage:
```
  (hbnb) quit
```

You can type any of the commands at the `(hbnb)` prompt to interact with the console.

### Running Tests

To execute all the tests, use the following command:

```
$ python3 -m unittest discover tests
```

If you want to run a specific test file, you can do so by specifying the file name:

```
$ python3 -m unittest tests/test_models/test_city.py
```
=======
This is the Airbnb Console project. It allows you to interact with the Airbnb system through a command-line interface.

First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine
What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object
>>>>>>> 24103b9f0f67f6e0446e8bbc4fe21666dfd27f0b
