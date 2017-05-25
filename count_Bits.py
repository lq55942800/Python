#codoing=utf-8

'''

Write a function that takes an (unsigned) integer as input, and returns the number of bits that are equal to

one in the binary representation of that number.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

'''



def countBits(n):
    bits = bin(n)
    L = []
    count = 0

    for i in bits:
        L.append(str(i))

    for i in L:
        # print (j)
        if i=='1':
            count+=1
        else:
            pass
    return count

# def countBits(n):
#     return bin(n).count("1")

print(countBits(1234))