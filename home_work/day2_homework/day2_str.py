"""
任务1-找出所有L开头的人名
任务2-按照年龄进行排序
任务3-找出所有女性用户的信息
"""
# 任务1-找出所有L开头的人名
re_1 = []
re_3 = []
mp = []
delete_space = []
# 读取文件
with open("personal_information", "r",encoding="utf-8") as f:
    lines = f.readlines()
    # print(lines)
    # 去除换行符
    for line in lines:
        line = line.rsplit()
        delete_space.append(line)
    # print(delete_space)


for d_list in delete_space:
    for d_l in d_list:
        # item = ['Lucy', '18601914231', '男', '19890218']
        items = d_l.split("|")

# 任务1
        if items[0].startswith("L") == True:
            re_1.append(items[0])
# 任务3
        if items[2] == "女":
            re_3.append(items)

        mp.append(items)

# 使用冒泡排序完成成任务2
n = len(mp)

for i in range(n):
    for j in range(0, n-i-1):
        if mp[j][3] > mp[j+1][3]:
            mp[j] , mp[j+1] = mp[j+1], mp[j]

print(re_1)
print(re_3)
print(mp)
