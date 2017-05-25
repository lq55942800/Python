#coding=utf-8
'''
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line.
 Each of them has a single 100, 50 or 25 dollars bill. A "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly
in the order people follow in the line?

Return YES, if Vasya can sell a ticket to each person and give the change. Otherwise return NO.

'''

def tickets(*People):
    count_25 = 0
    count_50 = 0
    count_100 = 0
    for i in People:
        if i==25:
            count_25+=1
        elif i==50:
            count_50+=1
        else:
            count_100+=1

    if count_100*100-count_50*50-count_25*25>25:
        return "NO"
    elif (count_100*100-count_50*50-count_25*25==0 or count_100*100-count_50*50-count_25*25==25):
        return "YES"
    else:
        if count_50*50-count_25*25>25:
            return "NO"
        elif (count_50*50-count_25*25==25 or count_50*50-count_25*25==0):
            return "YES"
        else:
            return "YES"



print (tickets([25,25,50]))