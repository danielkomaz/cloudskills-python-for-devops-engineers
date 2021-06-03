# Week 2 - Project 4 - Creating and using types

In programming, data types are a very important concept.

In python variables can store data of different types.

The following data types are built-in by default into python:

| Category        | Data Type                          |
| --------------- | ---------------------------------- |
| Text Type:      | `str`                              |
| Numeric Types:  | `int`, `float`, `complex`          |
| Sequence Types: | `list`, `tuple`, `range`           |
| Mapping Type:   | `dict`                             |
| Set Types:      | `set`, `frozenset`                 |
| Boolean Type:   | `bool`                             |
| Binary Types:   | `bytes`, `bytearray`, `memoryview` |

Even though Python uses data types it is not strict about which data type is hold by a variable.  
If no type is specified for a variable it is possible to assign a `str`to a variable and replace it with an `int` later in the code without error.  
Therefore it is considered good practice to define the type of a variable if possible.
