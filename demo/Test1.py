#coding=UTF-8

sum=0
for x in range(10):
    sum=x*x
    print (sum)

a=[1,2,3]
print(a)
a[2]=4
print(a)

for x in range(11):
    print(x,'love python')

classmate=[1,2,3,4]
classmate.append(5)
classmate.insert(0,9)

print (classmate)
classmate.pop()

print(classmate)
classmate[0]=0
print(classmate)
print(len(classmate))

t=['a','b','c',['A','B']]
t[3][0]='X'
t[3][1]='Y'
print(t)

