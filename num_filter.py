#coding=utf-8

def solution(number):
    count = 0
    for i in range(1,number):
        if i%3==0 or i%5==0:
            count+=i
    return count

print (solution(10))