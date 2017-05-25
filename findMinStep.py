#coding=utf-8
'''
Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W).
You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place).
Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.


Examples:

Input: "WRRBBW", "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW

Input: "WWRRBBWW", "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty

Input:"G", "GGGGG"
Output: 2
Explanation: G -> G[G] -> GG[G] -> empty

Input: "RBYYBBRRB", "YRBGB"
Output: 3
Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty
'''


import re

def findMinStep(board,hand):
    L = []
    L1 = []
    for i in hand:
        for j in range(0,len(board)+1):
            new_board = board[:j]+i+board[j:]
            trans_str = match_word(new_board)
            # print(trans_str)
            L.append(trans_str)
    print(L)

# 拼接消除后的字符串
def new_string(get_str):
    another_str =  str(get_str[0]+get_str[1])
    return another_str
# 正则匹配要消除的字符串，如果有返回列表，如果没有，则返回新字符串
def match_word(args):
    pattern = re.compile(r'RRR|YYY|BBB|GGG|WWW')
    match = pattern.search(args)
    if match:
        return new_string(pattern.split(args))
    else:
        return args







findMinStep("WRRBBW", "RB")