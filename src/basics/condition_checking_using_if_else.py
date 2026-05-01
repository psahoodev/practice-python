#!/usr/bin/env python3

print('-' * 50)

var_10 = True
var_11 = [1, 2, 3.4, True, [5,6,7], "List items"]

if (var_10):
    print(var_11)
else:
    print(f"Change value of {var_10} to False in order to print this")

print('-' * 50)

if (not False):
    print("This will be executed since False condition is negated with not")
else:
    print("This was not executed since condition was 0/None/False")

if(-2):
    print("-2 is also a satisfying condition since anything other than 0/None/False works")
else:
    print("-2 is not a satisfying condition")

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
