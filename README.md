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
guillaume@ubuntu:~/AirBnB$ 
```
```
AirBnB$ ./console.py
(hbnb) EOF
guillaume@ubuntu:~/AirBnB$ 
```

**help**
**create**
**show**
**destroy**
**all**
**update**