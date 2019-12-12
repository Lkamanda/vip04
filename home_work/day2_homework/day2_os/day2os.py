# 任务1-将该目录下的文件按照后缀进行分类，然后分别新建且放入不同的文件夹内，比如txt文件放入txt目录下等
import os

def create_fil(path):
    with open(path,"w") as f:
        pass

# print(os.path.abspath(os.path.dirname(__file__)))
# os.walk  当前路径下所有非目录子文件

# 1.获取当前的目录
ml = os.path.abspath(os.path.dirname(__file__))
print(ml)
# new_b :存放当前目录下已经存在的名称
new_b = []
# 需要创建的目录的集合
new_c = []

dict1 = {}
for files in os.walk(ml):
    print()
    for b in files[1]:
        new_b.append(b)
    for file in files[2]:
        # 根据点来进行切割
        s = file.split(".")

        # 将s列表中的俩个值分别作为k,v 加入字典
        dict1[s[0]] = s[1]
        if s[1] != 'py':
            # 新建目录
            new_c.append(s[1])
            for i in new_c:
                if i not in new_b:
                    os.mkdir(s[1])

            # 新建文件夹
            for d in list(dict1.values()):
                print(d)
                if d == s[1]:

                    # 路径拼接
                    new_path = os.path.join(ml,"./{}".format(s[1]), file)
                    print(new_path)
                    create_fil(new_path)









