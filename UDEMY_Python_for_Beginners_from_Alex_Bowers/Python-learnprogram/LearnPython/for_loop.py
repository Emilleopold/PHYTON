for a in [0,1,2,3,4]:
    print(type(a),a)
        
for s in 'String':
    print(type(s),s)  

for key,data in enumerate('strings'):
    if key % 2 == 0:
        print('The letter {} is in an even location'.format(data))
        
for i in range(1,10):
    print('This is i = {} with type of {}'.format(i, type(i)))
    