#coding=utf-8
'''

Given two integers, which can be positive and negative,find the sum of all the numbers between including them too and return it.
If both numbers are equal return a or b.

'''
def get_sum(a,b):
    c = b-a
    L = []
    count = 0
    for i in range(c+1):
        L.append(a+i)
    #print(L)
    for i in L:
        count+=i
    print(count)

get_sum(1,1)

'''
def get_sum(a,b):
    return sum(xrange(min(a,b), max(a,b)+1))
'''