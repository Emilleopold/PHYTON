list = [7,8,12,4,9,5,6] # Braucht 5 Durchlaeufe
#list = [8,7,12,4,9,6,5] # Braucht 6 Durchlaeufe
# list = [8,7,12,13,9,6,5] # Braucht 6 Durchlaeufe 

length = len(list)
print(length)

for M in range(0,length-1):
    swap = False
    for N in range(0,length-1):
        if list[N] > list[N+1]:
            temp = list[N]
            list[N] = list[N+1]
            list[N+1] = temp
            swap = True
        print(M,N)
    print(list, swap)
    if swap == False:
        print('Break')
        break
print(list, 'Finished')