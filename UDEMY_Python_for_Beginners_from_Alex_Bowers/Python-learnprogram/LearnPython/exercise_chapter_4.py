F0,F1 = 0,1
n = 2
Fn = 0
while Fn < 100:
    Fn = F0 + F1
    F0 = F1
    F1 = Fn 
    print(Fn)
print('Finished')