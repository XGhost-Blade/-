def right_step1(old):
    while True:
        for a in range(4):#a循环四次
            for b in range(3):#b循环三次
                if old[a][b] != '    ' and old[a][b+1]=='    ':#如果当前做表不为空，而右边为空
                    old[a][b],old[a][b+1] = old[a][b+1],old[a][b]#将两者调换位置
        count = 0
        for row in list: #在列表行内循环
            judge_list = []#建立新的列表 judge
            for number in row:#number在行内循环
                judge_list.append(str(number))#将number强制转化为字符串添加到新建列表的最后一项
            judge_str = ''.join(judge_list)#引用网络https://blog.csdn.net/lanseguhui/article/details/80338332
            judge_str = judge_str.strip()
            if '    ' in judge_str:#如果’’在judge_str里
                break #终端当前循环执行
            else:
                count += 1
        if count == 4:#如果等于4
            break #中断当前循环执行
            return old
def right_step2(old):
    global score
    for i in range(4):
        if old[i][3] != '    ' and old[i][3] == old[i][2]:
            old[i][3] = '%4d'%(int(old[i][3])*2)
            old[i][2] = '    '
            score += int(old[i][3])
            if old[i][1] != '    ' and old[i][1] == old[i][0]:
                old[i][1] = '%4d'%(int(old_list[i][1])*2)
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
