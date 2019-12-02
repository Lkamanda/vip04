a = 1

b= 2.5

c ='happy'

d = "let's go"

#
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
#
# # 不管输入什么类型都为str
# a = input('请输入一个整数：')
# print(a)
# print(type(a))

# a, b = input('please').split('.')

a = 1
b = 1.5
c = 'str'
print(("%d,%f,%s"%(a,b,c)))

print('a和b的知：', a,b)

print('a的知为%d,b的值为%s'%(a,b))

print('a的知为：{}, b的知为：{}'.format(a,b))

print(f"a的知为：{a},b的值为:{b}")

print('%03d'%a)
print('%.2f'%a)


print(f"a的知为：{a+1},b的值为:{b}")

# 有符号整数
# 无符号帧数

#tuple 元祖 元祖的值不可改变，list 可以改变
s = (1, 2.5, 'much')

l = [i for i in range(1,10)]
print(l)
tp = tuple(l)
print(type(tp))
print(tp[-3])

print(tp[3:8:2])

l1 = list(range(1,1000))

a  = [1,2,3,4,5]
a.reverse()
print(a)




a = [11,13,5,7,0,56,23,34,72]

s= {"a":10, 'b':20, 'c':30}
print(s.items())

# 分别定义一个集合和字典
# 1-为集合和字典分别插入元素55 ： d:55
# 2分别删除集合和字典内的一个元素
# 3去除字典内的所有值（value）和集合组合一个列表
a = {1,5,7}
d1 = {}
print(type(d1))
a.add(55)
a = set(a)

d1['d']=55
print(d1)


a.remove(55)
del d1['d']
print(d1)

d1 = {"a":1, "b":2, c:"3"}
value_list = list(d1.values())
value_list.extend(list(a))
print(value_list)



a = [7,5,4,2,8]
a.sort()
print(a)
a.reverse()
print(a)

#
# list1 = [1, 2, 3]
# a = input('输入')
# a = int(a)
# if a in list1:
#     print('happy')
#     list1[list1.index(a)] += 1
# else:
#     print('sad')
# print(list1)


# a = int(input('输入:'))
#
# if 90 <= a and a <= 100:
#     print('A')
# elif 80<= a <90:
#     print('B')
# elif 70<= a < 80:
#     print('c')
# elif 60<= a < 70:
#     print('D')
# else:
#     print('E')
#

# sum = 0
# for i in range(1,101):
#     print(i)
#     sum += i
# print(sum)

sum = 0
n = 1
while n <=100 :

    sum += n
    n += 1
print(sum)
