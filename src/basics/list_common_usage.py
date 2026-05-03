#/usr/bin/env python3

list1 = [3, 4, 9, 1, 0, 10]
list2 = [5, 5, 5, 1]

print(f"list1 = {list1} \t## orginal\nlist2 = {list2} \t\t## orginal")
list1.extend(list2)
print(f"list1 = {list1} \t## list.extend(list2)")

# how list.sort() works when the items are of int type
list1.sort()
print(f"list1 = {list1} \t## list.sort()")

list1.reverse()
print(f"list1 = {list1} \t## list.reverse()")
print("-" * 50)

# how list.sort() works when the items are of str type
list3 = ['10', '9', '5', '5', '5', '4', '3', '1', '1', '0']
print(f"list3 = {list3} \t## orginal")
list3.sort()
print(f"list3 = {list3} \t## list.sort()")

print(f"list3.count('5') = {list3.count('5')} \t## list.count([target item value])")
print(f"list3.index('5') = {list3.index('5')} \t## list.index([target item value])")
print(f"list3.index('5',7) = {list3.index('5',7)} \t## list.index([target item value], indexing starts from)")

print("-" * 50)
list4 = [0, 1, 2, 3, 4, 6]
print(f"list4 = {list4} \t## orginal")
print(f"list4.index(6) = {list4.index(6)} \t\t## list.index([target item value]) -> returns the item's index")
print(f"list4.pop() = {list4.pop()} \t\t## list.pop() -> returns the removed item")
print(f"list4.pop() = {list4.pop()} \t\t## list.pop() -> returns the removed item")
print(f"list4 = {list4} \t\t## current value")
print(f"list4.remove(1) = {list4.remove(1)} \t\t## list.remove([target item value]) -> None")
print(f"list4 = {list4} \t\t## current value")
print(f"list4.clear() = {list4.clear()} \t\t## list.clear() -> None")
print(f"list4 = {list4} \t\t\t## current value")
list4.insert(2,1)
list4.insert(2,1)
print(f"list4.insert(2,1) \t\t## executed twice")
print(f"list4 = {list4} \t\t\t## current value")
list4.extend([2])
print(f"list4 = {list4} \t\t## After list4.extend([2])")
list4.insert(0,0)
print(f"list4 = {list4} \t\t## After list4.insert(0,0)")
print(f"list4 = {list4} \t\t## current value")

#print(f"list4.pop() = {list4.pop()} \t## list.pop()")
#print(f"list4.index('5',7) = {list4.index('5',7)} \t## list.index([target item], indexing starts from)")

print("-" * 50)


#print(f"{list_03} before list_01.sort() returns {list_03.sort()} but sorts in-place {list_01}")
#list_10 = []
#list_08.extend(list_02)
#list_08.extend(list_02)