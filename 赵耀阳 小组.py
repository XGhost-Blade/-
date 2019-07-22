import random
import copy

# 分数
score = 0
# 开始界面
def start():#************

    list = [['    ', '    ', '    ', '    '], ['    ', '    ', '    ', '    '], ['    ', '    ', '    ', '    '], ['    ', '    ', '    ', '    ']]
   #定义一个列表，列表里有四项，列表是以竖向的形式展现的，这里就充当了2048游戏的边界
    i = 0#定义i等于0，有一个数输入
    while i < 2:#当i满足小于2时，会一直重复以下语句
        x = random.randint(0,3)#x整数的随机生成范围在0到3之间，但不包括3
        y = random.randint(0,3)#y整数的随机生成范围在0到3之间，但不包括3，其中randint的意思为模块random中的一个程序
        if list[y][x] == '    ':
            list[y][x] = '%4d'%2#二维数组，即原来的数组形成一种类似于田字格的形式，即2048的表格
            i += 1#执行完上述命令时，输出的i会重新+1，如果满足i<2，会重新执行while命令
    return list#当i不满足<2时，返回原列表，此时x与y就相当于2048游戏里开始出现的数字

# 将列表打印出游戏界面的效果
def print_number(li):#定义函数，print_number(li)
    for row in li:#row在li里面循环
        for number in row:#number在row里面循环
            print(number,end='|')
        print()#输出函数

