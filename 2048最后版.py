
import random
import copy

# 分数
score = 0
# 开始界面
def start():
    list_2048 = [['    ', '    ', '    ', '    '], ['    ', '    ', '    ', '    '], ['    ', '    ', '    ', '    '], ['    ', '    ', '    ', '    ']]
    i = 0
    while i < 2:
        x = random.randint(0,3)
        y = random.randint(0,3)
        if list_2048[y][x] == '    ':
            list_2048[y][x] = '%4d'%2
            i += 1
    return list_2048

# 将列表打印出游戏界面的效果
def print_number(li):
    for row in li:
        for number in row:
            print(number,end='|')
        print()

# down_step1 是将游戏界面里面所有的元素堆在下面，使中间没有空隙
def down_step1(old):
    while True:
        for x in range(3):
            for y in range(4):
                if old[x][y] != '    ' and old[x+1][y] == '    ':
                    old[x][y],old[x+1][y] = old[x+1][y],old[x][y]
        count = 0
        for y in range(4):
            judge_list = []
            for x in range(4):
                judge_list.append(str(old[x][y]))
            judge_str = ''.join(judge_list)
            judge_str = judge_str.strip()
            if '    ' in judge_str:
                break
            else:
                count += 1
        if count == 4:
            break
    return old

# down_step2 是将上下相邻且相同的数字合并，因为是向下移动，故判断的时候是从下像上判断，这点很重要。
def down_step2(old):
    global score
    for x in range(4):   # 将前面处理好，挨着紧凑的数据来判断最后两项是否相同，若相同就将两项合并
        if old[3][x] != '    ' and old[3][x] == old[2][x]:
            old[3][x] = '%4d'%(int(old[3][x]) * 2)
            old[2][x] = '    '
            score += int(old[3][x])
            if old[1][x] != '    ' and old[1][x] == old[0][x]:
                old[1][x] = '%4d'%(int(old[1][x]) * 2)
                old[0][x] = '    '
                score += int(old[1][x])
        elif old[2][x] != '    ' and old[2][x] == old[1][x]:
            old[2][x] = '%4d'%(int(old[2][x]) * 2)
            old[1][x] = '    '
            score += int(old[2][x])
        elif old[1][x] != '    ' and old[1][x] == old[0][x]:
            old[1][x] = '%4d'%(int(old[1][x]) * 2)
            old[0][x] = '    '
            score += int(old[1][x])
    return old
'''
down 是中和两个步骤，然后在把处理完的元素堆在下面。
这里没有用循环处理，是因为要让玩家每操作一次，也只变动一次，
操作一次，而变动多次会使玩家捉摸不到游戏的规律性
'''
def down(old):
    judge_list = copy.deepcopy(old)
    old = down_step1(old)
    old = down_step2(old)
    old = down_step1(old)
    if judge_list == old:
        return old
    if old[0].count('    ') + old[1].count('    ') + old[2].count('    ') + old[3].count('    ') >= 2:
        k = 0
        while k < 2:
            x = random.randint(0,3)
            y = random.randint(0,3)
            if old[y][x] == '    ':
                old[y][x] = '%4d'%2
                k += 1
    elif old[0].count('    ') + old[1].count('    ') + old[2].count('    ') + old[3].count('    ') == 1:
        k = 0
        while k < 1:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if old[y][x] == '    ':
                old[y][x] = '%4d'%2
                k += 1
    else:
        pass
    return old

def up_step1(old):
    while True:
        for x in range(3,0,-1):
            for y in range(4):
                if old[x][y] != '    ' and old[x-1][y] == '    ':
                    old[x][y],old[x-1][y] = old[x-1][y],old[x][y]
        count = 0
        for y in range(4):
            judge_list = []
            for x in range(4):
                judge_list.append(str(old[x][y]))
            judge_str = ''.join(judge_list)
            judge_str = judge_str.strip()
            if '    ' in judge_str:
                break
            else:
                count += 1
        if count == 4:
            break
    return old
def up_step2(old):
    global score
    for x in range(4):   # 将前面处理好，挨着紧凑的数据来判断最后两项是否相同，若相同就将两项合并
        if old[0][x] != '    ' and old[0][x] == old[1][x]:
            old[0][x] = '%4d'%(int(old[0][x]) * 2)
            old[1][x] = '    '
            score += int(old[0][x])
            if old[2][x] != '    ' and old[2][x] == old[3][x]:
                old[2][x] = '%4d'%(int(old[2][x]) * 2)
                old[3][x] = '    '
                score += int(old[2][x])
        elif old[1][x] != '    ' and old[1][x] == old[2][x]:
            old[1][x] = '%4d'%(int(old[1][x]) * 2)
            old[2][x] = '    '
            score += int(old[1][x])
        elif old[2][x] != '    ' and old[2][x] == old[3][x]:
            old[2][x] = '%4d'%(int(old[2][x]) * 2)
            old[3][x] = '    '
            score += int(old[2][x])
    return old
def up(old):
    judge_list = copy.deepcopy(old)
    old = up_step1(old)
    old = up_step2(old)
    old = up_step1(old)
    if judge_list == old:
        return old
    if old[0].count('    ') + old[1].count('    ') + old[2].count('    ') + old[3].count('    ') >= 2:
        k = 0
        while k < 2:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if old[y][x] == '    ':
                old[y][x] = '%4d'%2
                k += 1
    elif old[0].count('    ') + old[1].count('    ') + old[2].count('    ') + old[3].count('    ') == 1:
        k = 0
        while k < 1:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if old[y][x] == '    ':
                old[y][x] = '%4d'%2
                k += 1
    else:
        pass
    return old

def left_step1(old):
    while True:
        for x in range(4):
            for y in range(3,0,-1):
                if old[x][y] != '    ' and old[x][y-1]=='    ':
                    old[x][y],old[x][y-1] = old[x][y-1],old[x][y]
        count = 0
        for row in old:
            judge_list = []
            for number in row:
                judge_list.append(str(number))
            judge_str = ''.join(judge_list)
            judge_str = judge_str.strip()
            if '    ' in judge_str:
                break
            else:
                count += 1
        if count == 4:
            break
    return old
def left_step2(old):
    global score
    for i in range(4):
        if old[i][0] != '    ' and old[i][0] == old[i][1]:
            old[i][0] = '%4d'%(int(old[i][0])*2)
            old[i][1] = '    '
            score +=int(old[i][0])
            if old[i][2] != '    ' and old[i][2] == old[i][3]:
                old[i][2] = '%4d'%(int(old[i][2])*2)
                old[i][3] = '    '
                score += int(old[i][2])
        elif old[i][1] != '    ' and old[i][1] == old[i][2]:
            old[i][1] ='%4d'%(int(old[i][1])*2)
            old[i][2] = '    '
            score += int(old[i][1])
        elif old[i][2] != '    ' and old[i][2] == old[i][3]:
            old[i][2] ='%4d'%(int(old[i][2])*2)
            old[i][3] = '    '
            score += int(old[i][2])
    return old
def left(old):
    judge_list = copy.deepcopy(old)
    old = left_step1(old)
    old = left_step2(old)
    old = left_step1(old)
    if judge_list == old:
        return old
    if old[0].count('    ') + old[1].count('    ') + old[2].count('    ') + old[3].count('    ') >= 2:
        k = 0
        while k < 2:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if old[y][x] == '    ':
                old[y][x] = '%4d'%2
                k += 1
    elif old[0].count('    ') + old[1].count('    ') + old[2].count('    ') + old[3].count('    ') == 1:
        k = 0
        while k < 1:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if old[y][x] == '    ':
                old[y][x] = '%4d'%2
                k += 1
    else:
        pass
    return old

def right_step1(old):
    while True:
        for x in range(4):
            for y in range(3):
                if old[x][y] != '    ' and old[x][y+1]=='    ':
                    old[x][y],old[x][y+1] = old[x][y+1],old[x][y]
        count = 0
        for row in old:
            judge_list = []
            for number in row:
                judge_list.append(str(number))
            judge_str = ''.join(judge_list)
            judge_str = judge_str.strip()
            if '    ' in judge_str:
                break
            else:
                count += 1
        if count == 4:
            break
    return old
def right_step2(old):
    global score
    for i in range(4):
        if old[i][3] != '    ' and old[i][3] == old[i][2]:
            old[i][3] = '%4d'%(int(old[i][3])*2)
            old[i][2] = '    '
            score += int(old[i][3])
            if old[i][1] != '    ' and old[i][1] == old[i][0]:
                old[i][1] = '%4d'%(int(old[i][1])*2)
                old[i][0] = '    '
                score += int(old[i][1])
        elif old[i][2] != '    ' and old[i][2] == old[i][1]:
            old[i][2] ='%4d'%(int(old[i][2])*2)
            old[i][1] = '    '
            score += int(old[i][2])
        elif old[i][1] != '    ' and old[i][1] == old[i][0]:
            old[i][1] ='%4d'%(int(old[i][1])*2)
            old[i][0] = '    '
            score += int(old[i][1])
    return old
def right(old):
    judge_list = copy.deepcopy(old)
    old = right_step1(old)
    old = right_step2(old)
    old = right_step1(old)
    if judge_list == old:
        return old
    if old[0].count('    ') + old[1].count('    ') + old[2].count('    ') + old[3].count('    ') >= 2:
        k = 0
        while k < 2:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if old[y][x] == '    ':
                old[y][x] = '%4d' % 2
                k += 1
    elif old[0].count('    ') + old[1].count('    ') + old[2].count('    ') + old[3].count('    ') == 1:
        k = 0
        while k < 1:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if old[y][x] == '    ':
                old[y][x] = '%4d' % 2
                k += 1
    else:
        pass
    return old

###################################################################
old = start()
print_number(old)
while True:
    # 当玩家还是Ture（存活）的时候，根据用户输入做出相应的移动
    print()
    user_input = input('请输入你要移动的方向[上(w)下(s)左(a)右(d)]:')
    print()
    if user_input == 'w':
        old = up(old)
        print_number(old)
        print()
        print('目前得分：%d 分'%score)
    elif user_input == 's':
        old = down(old)
        print_number(old)
        print()
        print('目前得分：%d 分' % score)
    elif user_input == 'a':
        old = left(old)
        print_number(old)
        print()
        print('目前得分：%d 分' % score)
    elif user_input == 'd':
        old = right(old)
        print_number(old)
        print()
        print('目前得分：%d 分' % score)
    else:
        print()
        print('输入错误！请输入正确的方向！')
        print_number(old)
    # 游戏的终止条件：
    # 判断界面是否还有空位
    if old[0].count('    ') + old[1].count('    ') + old[2].count('    ') + old[3].count('    ') == 0:
        # 判断每一个数相邻是否还有相同的数字
        count = 0
        for i in range(4):          # 判断横排
            for j in range(3):
                if old[i][j] == old[i][j+1]:
                    count += 1
        for x in range(4):
            for y in range(3):
                if old[y][x] == old[y+1][x]:
                    count += 1
        if count == 0:
            print('很遗憾，游戏结束！')
            print('您的最终得分：%d 分' % score)
            break
#################################################################################
