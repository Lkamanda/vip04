"""
任务1-找出所有L开头的人名
任务2-按照年龄进行排序
任务3-找出所有女性用户的信息
"""
# 任务1-找出所有L开头的人名

# delete_space = []
# with open("personal_information", "r",encoding="utf-8") as f:
#     lines = f.readlines()
#     print(lines)
#     # 去除换行符
#     for line in lines:
#         line = line.rsplit()
#         delete_space.append(line)
#     print(delete_space)
#
# for d_list in delete_space:
#     for d_l in d_list:
#         d_l.split("|")
#     print()

a = ['Lucy|18601914231|男|19890218']
for i in a:
    i.