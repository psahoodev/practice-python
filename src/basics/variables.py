#!/usr/bin/env python3

var_01 = 108
var_02 = 4.5

print("var_01 has value", var_01, ",other one var_02 =", var_02)
print('-' * 50)
var_03 = 'Hello world !!'
var_04 = "Good job,\nThank you..."
var_05 = """This type of string is mostly used as doc strings.
You may also use when you a string with multiple lines.
"""
var_06 = r"C:\Users\All Users\Desktop\newfile.txt"

print(f"{var_03} - printed as it is")
print(f"{var_04} - print with new line in between due to '\\n'")
print(f"{var_05}")
print(f"{var_06} - raw string does not respect the escape characters")

print('-' * 50)

var_07 = True
var_08 = [1, 2, 3.4, True, [5,6,7], "List items"]

if (var_07):
    print(var_08)

print('-' * 50)

if (not False):
    print("This will be executed since False condition is negated with not")
else:
    print("This was not executed since condition was 0/None/False")

if(0):
    print("0 is a satisfying condition")
else:
    print("0 is not a satisfying condition")

if(''):
    print("'' is a satisfying condition")
else:
    print("'' is not a satisfying condition")

if(None):
    print("None is a satisfying condition")
else:
    print("None is not a satisfying condition")

if():
    print("Empty is a satisfying condition")
else:
    print("Empty is not a satisfying condition")

print('-' * 50)
