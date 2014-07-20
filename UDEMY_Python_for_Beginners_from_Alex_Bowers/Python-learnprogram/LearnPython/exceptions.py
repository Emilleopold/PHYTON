tuple = (1,2,3,4,5)
try:
    tuple.append(6)
    for each in tuple:
        print(each)
except AttributeError as e:
    print('Error formed: ' , e)
except IOError as e:
    print('File not found:', e)


# Alternative, nicht so gut    
    tuple = (1,2,3,4,5)
try:
    tuple.append(6)   
except AttributeError as e:
    print('Error formed: ' , e)
else:
    for each in tuple:
        print(each)
