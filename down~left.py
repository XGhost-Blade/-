#encoding:utf-8
###By DaveZ **start
def down_step1(old):
    while True:
        for x in range(3):
            for y in range(4):
                if ((old[x][y]!=' ') and (old[x+1][y])==' '):
                    old[x][y] , old[x+1][y] = old[x+1][y] , old[x][y]
                    count=0
        for y in range(4):
            judge_list = []
            for x in range(4):
                judge_list.append(str(old_list[x][y]))
            judge_str = ''.join(judge_list)
            judge_str = judge_str.strip()
            if '    ' in judge_str:
                break
            else:
                count += 1
        if count == 4:
            break
    return old


#
# #因为是向下移动，注意判断是从下到上
def down_step2(old):
    global score
    for x in range(4):
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
down把处理完的元素堆在下面
'''
def down(old):#生成down操作完的列表
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
    for x in range(4):   # 依次判断相邻两项是否相同，若相同则合并
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
def up(old):    #生成变更过的列表
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

#同理，可以创造进行向左操作的函数
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

##By DaveZ Ended




