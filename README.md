# AirBnB_clone

# -    CONSOLE    -

- The console is a command interpreter to manage, AirBnB objects.
    - create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file

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

**help** - shows how a command works - Usage: " help " or " help command_name "

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

**create** - creates new instance of given class - Usage: " create class_name "
- create returns the ID of the instance created

```
AirBnB$ ./console.py
(hbnb)
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
```
**show**
**destroy**
**all**
**update**