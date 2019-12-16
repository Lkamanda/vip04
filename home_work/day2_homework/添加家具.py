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

    def __init__(self, hx, mj):
        self.hx = hx
        self.mj = mj
        self.temporary_mj = mj

    def  add(self, item):
        print(type(item.mj))
        print(type(self.temporary_mj))
        if item.mj >self.temporary_mj:
            print("房间剩余面积不足，不能添加新家具")
        else:
            self.temporary_mj -= item.mj
            print(self.temporary_mj)


class Furniture(object):
    def __init__(self, name, mj):
        self.name = name
        self.mj = mj




bed = Furniture(name='床', mj=4)
wardrobe = Furniture(name="衣柜", mj=2)
table = Furniture(name="餐桌", mj=1.5)
house = House('俩室一厅', 200)
house.add(bed)