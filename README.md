# AirBnB_clone

# -    CONSOLE    -

- The console is a command interpreter to manage, AirBnB objects.
    - Create a new object (ex: a new User or a new Place)
    - Retrieve an object from a file, a database etc…
    - Do operations on objects (count, compute stats, etc…)
    - Update attributes of an object
    - Destroy an object

## Execution
### Interactive mode(How to Start it):

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
```

### Non-Interactive mode(How to Start it):

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Implemented Commands(How to Use it):

**quit** && **EOF** - Both quit the console.

```
AirBnB$ ./console.py
(hbnb) quit 
/AirBnB$ 
```
```
AirBnB$ ./console.py
(hbnb) EOF
AirBnB$ 
```

**help** - shows how a command works 
- Usage: " help " or " help command_name "

```
AirBnB$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

```

**create** - creates new instance of given class 
- Usage: " create class_name "
- create returns the ID of the instance created

```
AirBnB$ ./console.py
(hbnb)
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
```

**show** - Prints the string representation of an instance based on the class name and id
- Usage: " show class_name id "
```
AirBnB$ ./console.py
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
```

**destroy** - Deletes an instance based on the class name and id
- Usage: " destroy class_name id "
```
AirBnB$ ./console.py
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
```

**all** - Prints all string representation of all instances based or not on the class name
- Usage: " all " or " all class_name "
```
AirBnB$ ./console.py
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
```

**update** - Updates an instance based on the class name and id by adding or updating attribute
- Usage: " update class_name id attribute_name attribute_value "
```
AirBnB$ ./console.py
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
```

## - ERROR - Handling - Messages -

| **ERROR**                       | **Description**                                                |
|---------------------------------|----------------------------------------------------------------|
| `** class name missing **`      | *If the class name doesn’t exist:*                             |
| `** class doesn't exist **`     | *If the class name doesn’t exist:*                             |
| `** instance id missing **`     | *If the id is missing:*                                        |
| `** no instance found **`       | *If the instance of the class name doesn’t exist for the id:*  |
| `** attribute name missing **`  | *If the attribute name is missing:*                            |
| `** value missing **`           | *If the value for the attribute name doesn’t exist:*           |