# AirBnB_clone

# -    CONSOLE    -

- The console is a command interpreter to manage, AirBnB objects.
    - create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file

## Execution
### Interactive mode:

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

### Non-Interactive mode:

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