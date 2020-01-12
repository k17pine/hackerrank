for i in range(1, int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    #print(i*'{}'.format(*(i * [i])))
    #print(f'{i}'*i)
    #print(*(i * [i]), sep='')
    print(sum(map(lambda x: i * 10**x, range(i))))