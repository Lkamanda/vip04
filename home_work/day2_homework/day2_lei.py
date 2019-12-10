"""
练习：
a、定义一个学生类：Student、内部含有一个方法：study，实现打印：xx学习xx课程
b、定义一个类名：Student—学生、类内部含有一个属性：sno—学号，一个方法：study—学习，实现打印：学号为xx的学生，学习xx课程
"""
# a
class Student_a(object):
    def __init__(self, name, *course):
        self.name = name
        self.course = course

    def study(self):
        print("{0}学习{1}".format(self.name, self.course))

zj = Student_a("XL", "数学", "英语")
zj.study()

# b
class Student_b(object):
    def __init__(self, ano, *course):
        self.ano = ano
        self.course = course

    def study(self):
        print("学号为{0}的学生，学习{1}课程".format(self.ano,self.course))

student_b = Student_b(12,"数学","英语")
student_b.study()

"""
练习：
定义一个Teacher类，继承Person类，拥有自身的属性工号：gh，自身的方法：teach教课（课程）；
1、实现gh为xx的老师，教xx课
2、实现gh为xx老师，在xx上班，一月工资xx
3、名字是xx，工号为xx的老师，吃饭
"""


class Person(object):
    def __init__(self,name, work_place, gz):
        self.name = name
        self.work_place = work_place
        self.gz = gz

    def eat(self):
        return "{}吃饭".format(self.name)

    def work(self):
        print("在{}工作，一个月工资为{}".format(self.work_place, self.gz))


class Teacher(Person):
    def __init__(self,ano, name, course, work_place, gz):
        Person.__init__(self, name, work_place, gz)
        self.course = course
        self.ano = ano

    def teach(self):
        print("{0}为{1}老师，教{1}课程".format(self.name,self.course))
# 1，2
gh = Teacher(ano="001", name="gh", course="数学", work_place="学校", gz="5000")
gh.teach()
gh.work()
# 3 名字是xx，工号为xx的老师，吃饭
print("名字是{0}，工号为{1}的老师，{2}".format(gh.name, gh.ano, gh.eat()))


# 1、打印小猫爱吃鱼，小猫要喝水
class Cat(object):
    def eat(self):
        print('小猫爱吃鱼')

    def drink(self):
        print('小猫要喝水')

cat = Cat()
cat.eat()
cat.drink()

"""
2、小明爱跑步，爱吃东西。
1）小明体重75.0公斤
2）每次跑步会减肥0.5公斤
3）每次吃东西体重会增加1公斤
4）小美的体重是45.0公斤
"""

class Human1(object):
    # dw = '公斤'
    def __init__(self, weight, name):
        self.weight = weight
        self.name = name

    def run(self):
        self.weight -= 0.5
        self.tz()

    def eat(self):
        self.weight += 1
        self.tz()

    dw = '公斤'
    def tz(self):
        print("{0}当前体重为：{1}{2}".format(self.name, self.weight, self.dw))

xm = Human1(weight=75,name="小明")
xm.run()
xm.eat()
mei = Human1(weight=45, name="小美")
mei.tz()

"""
3、摆放家具
需求：
1）.房子有户型，总面积和家具名称列表
   新房子没有任何的家具
2）.家具有名字和占地面积，其中
   床：占4平米
   衣柜：占2平面
   餐桌：占1.5平米
3）.将以上三件家具添加到房子中
4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
"""
class House(object):
    mj_d = "平米"

    def __init__(self, hx, mj, *furniture):
        self.hx = hx
        self.furniture = furniture
        self.mj = mj

    def return_mj(self):
        """
        :return:返回房子的剩余面积
        """
        temporary_mj = self.mj
        for f in self.furniture:
            temporary_mj -= f.mj
        return temporary_mj

    def return_fn(self):
        """返回家具名称列表"""
        fl = []
        for f in self.furniture:
            if f.name not in fl:
                fl.append(f.name)
        return fl

# 打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
    def return_all(self):
        # 判断房间是否有家具
        if self.furniture == ():
            temp_furniture = "新房子没有家具"
            print("输出:户型：{0}， 面积：{1}{3}, 家具：{2}".format(self.hx, self.mj, temp_furniture, self.mj_d))
        else:
            print("输出:户型:{0},总面积：{1}，剩余面积：{2}，家具名称列表{3}".format(self.hx, self.mj, self.return_mj(), self.return_fn()))


class Furniture(object):
    def __init__(self, name, mj):
        self.name = name
        self.mj = mj
    def rb(self):
        return self.mj

#需求：1)
new_house = House('俩室一厅', 70)
new_house.return_all()
#需求：2)
bed = Furniture(name='床', mj=4)
wardrobe = Furniture(name="衣柜", mj=2)
table = Furniture(name="餐桌", mj=1.5)
#需求：3)
old_house = House('俩室一厅', 70, bed, wardrobe, table)
old_house.return_all()


"""
4.士兵开枪
需求：
1）.士兵瑞恩有一把AK47
2）.士兵可以开火(士兵开火扣动的是扳机)
3）.枪 能够 发射子弹(把子弹发射出去)
4）.枪 能够 装填子弹 --增加子弹的数量

"""
class Solid(object):
    def __init__(self, name):
        self.name = name
    def shut(self,temp):
        if temp.shut() == 1:
            print('开火')

    def tz(self,temp):
        if temp.tz() == 1:
            print('装弹')

class Rob(object):
    def __init__(self, name):
        self.num = 0
        self.name = name
    def shut(self):
        """temporary_num = 0 作为一个状态，只有为1时候才能出发之后的事件"""
        temporary_sh = 0
        if self.num >0:
            self.num -= 1
            print(self.num)
            temporary_sh = 1
        else:
            print("弹夹空了，请装弹")
        return temporary_sh

    def tz(self):
        temporary_tz = 0
        if self.num <= 30:
            self.num = 30
            print(self.num)
            temporary_tz = 1
        else:
            print("已经到了最大容量")
        return temporary_tz

ak = Rob(name="ak47")
rs = Solid(name="瑞士")
rs.tz(ak)
rs.shut(ak)
rs.shut(ak)
rs.tz(ak)


