# -*- coding: latin1 -*-

def nprimo(nums):
    if nums < 2:
        return 'Nao Primo'
    for i in range(int(2), nums):
        if not nums % i:
            return 'Nao Primo'
    else:
        return 'Primo'


for j in range(1, 101):
    print j, nprimo(j)
