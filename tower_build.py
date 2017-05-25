#coding=utf-8
'''
输出*塔
'''
# def tower_builder(n):
    # 1,3,5,7,9
    # 1,2,3,4,5
    # 每一层的*数量为2n-1,每一层的空间为2n-1
    # for i in range(1,n+1):
        # 每层星星数
        # start_num = int(2*i-1)
        # 空格数量
        # null_num = int((2*n-1-(2*i-1))/2)
        # return (' '*null_num+'*'*start_num+' '*null_num)

def tower_builder(n):
    L = []
    for i in range(1,n+1):
        start_num = int(2*i-1)
        null_num = int((2*n-1-(2*i-1))/2)
        str = ' '*null_num+'*'*start_num+' '*null_num
        L.append(str)
    return L

tower_builder(6)