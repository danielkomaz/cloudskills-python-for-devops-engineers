# Global variable, defined outside of any function
globalName = "Dan"

def helloGlobal():
    print('Hello ' + globalName)

helloGlobal()

# Local variable, defined within a function
def helloLocal():
    localName = "Daniel"
    print('Hello ' + localName)

helloLocal()

# Runtime variable, passed intot he program when calling from outside

import sys

def helloRuntime(runtimeName):
    print('Hello ' + runtimeName)

runtimeVar = sys.argv[1]

helloRuntime(runtimeVar)
