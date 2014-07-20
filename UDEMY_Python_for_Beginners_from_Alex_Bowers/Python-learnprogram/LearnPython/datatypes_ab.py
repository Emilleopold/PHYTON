
# Numbers
#Integers
i = 150
print(type(i),i)

#float

f = 150.0
print(type(f),f)

#string

s = 'String'
m = '''\
Multi
Line
String\
'''

print(type(s),s)
print(type(m),m)

a = 'Hello'
s2 = 'String {}'.format(a)
print(s2)

#Lists and Tuples

# Tuples

t = (1,2,3,4)
print(type(t),t)

#List 
l = [1,2,3,4,5]
print(type(l),l)

#Array / Dictionary

d = {'one':1,'two':2}
d2 = dict(
          one = 1,
          two = 2)
print(type(d),d)
print(type(d2),d2)

#Boolean

t1 = True
t2 = False

if t1 == t2:
    print(t1) #True
else:
    print(t2) #False