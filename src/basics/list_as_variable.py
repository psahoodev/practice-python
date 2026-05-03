#!/usr/bin/env python3

list_01 = [1, 2, 3, 4, 5]
list_02 = [5,6,7]
list_03 = [True, "List items"]
list_04 = []

list_05 = list_01
list_06 = list_01.copy()
print(f"list_05 = list_01 # {list_05}")
print(f"list_06 = list_01.copy() # {list_06}")

list_01.append(6)
list_05.append(10)
list_06.append(11)
print(f"after append() the values of all 3 lists are :")
print(f"\tlist_01.append(6) \n\tlist_05.append(10) \n\tlist_06.append(11)")
print(f"List and its corresponding address and values are :")
print(f"list_01 = {id(list_01)} - {list_01}")
print(f"list_05 = {id(list_05)} - {list_05}")
print(f"list_06 = {id(list_06)} - {list_06}")
'''
print(f"list_01 = {list_01}")
print(f"list_05 = {list_05}")
print(f"list_06 = {list_06}")
'''

if (list_04):
    print(f"Value of {list_04} in if condition is True")
else:
    print(f"Value of {list_04} in if condition is False")

list_08 = []
list_08.append([1,2])
list_08.extend([1,2])
print(f"{list_08} after the append([1,2]) and extend([1,2])")

list_09 = ['a', 'b', 'c', [100, 101]]
list_04.extend(list_09)
print(f"{list_04} after the extend(['a', 'b', 'c', [100, 101]])")


print(f"{list_03} before list_01.sort() returns {list_03.sort()} but sorts in-place {list_01}")
#list_10 = []
#list_08.extend(list_02)
#list_08.extend(list_02)