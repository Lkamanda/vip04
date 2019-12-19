# 字符串操作

# 1。把字符串的第一个字符大写
a = "dsfsdjfhkj"
a.capitalize()
print(a)

# 返回 str 在 string 里面出现的次数，
a = "abc123abcab123abc485abc"
print(a.count("abc",0,10))

# 编码以及解码
b = a.encode(encoding="utf-8",errors='strict')
b.decode(encoding="gbk")
print(b)

# 检测str 是否包含在string 中，可以设置指定范围，如果是返回开始索引值，否则返回-1
a = "abc123abcab123abc485abcf"
print(a.find("3ab",1,10))
print(a.find("abt"))

# 检测字符串在指定范围内是否以指定字符串结尾
a = "abc123abcab123abc485abcf"
print(a.endswith('abcf'))
print(a.endswith('3', 0,6))

# find.index(str,beg,end) 和find方法一致，如果不存在会报个异常

# string.isalpha() string 至少有一个字符，并且所有字符都是字母否则返回True
a = "abc"
print(a.isalpha())

a = "123"
# 判断ste只含有数字
print("只含有数字" + str(a.isdigit()))
a = "sadf"
# 只含有小写 string.islower
print(a.islower())

# string.join(seq) 以string作为分隔符，将seq 中所有元素进行合并
ss = ['a', 'b', 'c']
s = "我是分隔符"
print(s.join(ss))

a ="   我sdfAd"
print(a.lower())
print(a)

# 去掉字符串左边的空格
print(a.lstrip())

# string.replace(str1, str2, num)  把string 中的str1替换成str2，num次

a = "  abababababab   "
print(a.replace("b","c",3))
print(a)
print(a.strip())


# string.swapcase() 大小写翻转

# string.upper() 将string中小写变为大写

# string.startswitch(obj, beg, end)检查字符串是否以obj结尾，beg ,end 范围

# strip.split(str, num) str为分隔符，仅分隔n个

a = "  abcabcabacbabab   "

print(a.split("c", 3))
print(a)
