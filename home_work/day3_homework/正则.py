import re

# 将正则表达式编译成Pattern
# pattern = re.compile(r'[%_&]')
# match = pattern.match('')
# print(match)
# print(match.group())

# 1、匹配一行文字的所有开头的字母内容
s="i love you not because of who you are, but because of who i am when i am with you"
content = re.findall(r"\b\w",s)
print(content)

# 匹配一行文字中的所有开头的数字内容
s="i love you not because 12sd 34er 56df e4 54434"
content = re.findall(r'\b\d',s)
print(content)

# 匹配包含字母和数字的行
s="i love you not because\n12sd 34er 56\ndf e4 54434"
content=re.findall(r"\w+",s)
print(content)

s="""se234 1987-02-09 07:30:00

    1987-02-10 07:25:00"""

# content = re.findall(r"\d{4}-\d{2}-\d{9}", s,re.M)
content=re.findall(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:", s)
print(content)

# 将每行中的电子邮件地址替换为你自己的电子邮件地址
s="""693152032_@qq.com, werksdf@163.com, sdf@sina.um

    sfjsdf@139.com, soifsdfj@134.com

    pwoeir423@123.cn"""

# content = re.findall(r"\w+@\w+.com",s)
# print(content)
# content=re.match(r'[0-9a-zA-Z_]{0,19}',s)
content = re.findall(r"[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn]{1,3}",s)
print(content)