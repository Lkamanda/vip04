import pymysql

# 连接database
conn = pymysql.connect(
    host="数据库地址",
    user="用户名",
    password="密码",
    database="数据库名",
    charset="UTF-8",
    port="端口号"
)

# 得到一个执行sql光标对象
cursor = conn.cursor()

sql = """"""
# 执行sql语句
cursor.excute(sql)
# 关闭光标对象
cursor.close()
# 关闭数据库链接
conn.close()