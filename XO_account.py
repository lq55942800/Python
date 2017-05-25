#coding=utf-8
'''

Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive.
 The string can contains any char.



'''
def xo(s):
    count_x = 0
    count_0 = 0
    if isinstance(s,str):
        for i in s:
            if i == 'x' or i == 'X':
                count_x+=1
            else:
                count_0+=1
    else:
        return False
    if count_x%2==0 and count_0%2==0:
        return True
    else:
        return False


print (xo('XXOOo'))