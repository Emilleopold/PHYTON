b = 'Hallo'
a = 'This is {} a string'.format(b)
print(a)

t = (1,2,3,4,5)
print(type(t),t)

x = [1,2,3,4,5]
x.append(6)
print(type(x),x)
print(type(x),x[2:4])

y = {'one':5,'two':2}
print(type(y),y)

dictionary = dict(
                  one = 1,
                  two = 'two'
             )
print(type(dictionary),dictionary)

boolean = False
print(type(boolean),boolean)

a,b,c = 1,2,3
if a==b:
    print(True)
else:
    print(False)