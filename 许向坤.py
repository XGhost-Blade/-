#启动游戏

old = start()
print_number(old_list)

while True:
    # 重复。玩家还是Ture（存活）的时候，根据用户输入做出相应的移动
    print()
    user_input = input('请输入你要移动的方向[上(w)下(s)左(a)右(d)]:')
    print()
    if user_input == "w":
        old = up (old)
        print_number(old)
        print()
        print('目前得分：%d 分'%score)
    elif user_input == "s":
        old = down(old)
        print_number(old)
        print()
        print('目前得分：%d 分'%score)
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
        print_number(old_list)

# 游戏的终止条件：

# 第一点：判断界面是否还有空位。
    if old[0].count('    ') + old[1].count('    ') + old[2].count('    ') + old[3].count('    ') == 0:
        # 第二点：判断每一个数相邻是否还有相同的数字。
        count = 0
        for i in range(4):          # 判断横排，循环。
            for j in range(3):
                if old[i][j] == old[i][j+1]:
                    count += 1
        for x in range(4):
            for y in range(3):
                if old[y][x] == old[y+1][x]:
                    count += 1
        if count == 0:
            print('很遗憾，您不行了！')
            print('您的最终得分：%d 分' % score)
            break
