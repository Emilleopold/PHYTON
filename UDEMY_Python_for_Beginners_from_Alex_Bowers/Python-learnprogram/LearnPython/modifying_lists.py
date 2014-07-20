list = [1,2,3,4,5,6,7,8,9,10,11,'one']
# Dadurch wir die 0 am Anfang eingefuegt
list.reverse()
list.append(0)
list.reverse()

print(list)

list = [1,2,3,4,5,6,7,8,9,10,11]

list.append(12)

print(list)

list = [1,2,3,4,5,6,7,8,9,10,11]

list.insert(4,20) # Fuegt den Wert 20 als Index 4 ein

print(list)

list = [1,2,3,4,5,6,7,8,9,10,11]

del list[4] # Entfernt den Index 4 -> hier die 5

print(list)

list = [1,2,3,4,5,6,7,8,9,10,11]

list.remove(4) # Entfernt den Wert 4

print(list)

list = [1,2,3,4,5,6,7,8,9,10,11]
list2 = [12,13,14]
list.extend(list2)

print(list)
