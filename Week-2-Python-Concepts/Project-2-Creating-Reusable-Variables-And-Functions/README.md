# Week 2 - Project 2 - Creating reusable variables and functions

There are 3 types of variables:

## Local Variables

Local variables are defined within a function and therefore only available within that function.

Example:

```Python
def helloLocal():
    localName = "Daniel"
    print('Hello ' + localName)

helloLocal()
```

## Global variables

Global variables are defined outside of functions and are valid throughout the whole program and can be used in multiple fuctions.

Example:

```Python
globalName = "Dan"

def helloGlobal():
    print("Hello" + globalName)

helloGlobal()
```

## Runtime Variables

Runtime variables are arguments passed into the program when calling it e.g. from the cli.

Example:

```Python
import sys

def helloRuntime(runtimeName):
    print('Hello ' + runtimeName)

runtimeVar = sys.argv[1]

helloRuntime(runtimeVar)
```

Now when you call the script with an argument, the argument will be used for the Hello output:

```Powershell
PS> python vars.py Mike
Hello Mike
```
