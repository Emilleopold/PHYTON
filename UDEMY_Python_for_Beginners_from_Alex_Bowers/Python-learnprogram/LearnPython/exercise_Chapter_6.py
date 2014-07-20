while True:
    data = input('Please enter your gender :\n')
    if data in ('m','M','f','F'):
        break
print('That was correct, your gender is : {}'.format(data))