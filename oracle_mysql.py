#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import cx_Oracle, pymysql
# python安装模块
# pip install cx_Oracle pip install pymysql
# 自己修改连接地址,下面是oralce的配置文件
# --------------------------
username = 'system'
passwd = 'oracle'
host='192.168.1.111'
port='1521'
sid ='xe'
# -----------------------------
# mysql配置文件
mysql_config = {
    'host': '192.168.1.11',
    'port': 3306,
    'user': 'zhang',
    'password': '123456',
    'db': 'cmdb',
    'charset': 'utf8',
}
dsn = cx_Oracle.makedsn(host,port,sid)
oracle_conn= cx_Oracle.connect(username,passwd,dsn)
# oracle_conn =cx_Oracle.connect('system/oracle@192.168.1.111:1521/xe')
# 取出想要插入mysql的数据,
select_sql_oracle = 'select * from app01_business'
oracle_cursor = oracle_conn.cursor()
oracle_sql = oracle_cursor.execute(select_sql_oracle)
obj = oracle_cursor.fetchall()
# print obj
mysql_conn = pymysql.connect(**mysql_config)
mysql_cursor = mysql_conn.cursor()
for i in obj:
    # 我的表只有3列,如有有多的请按照格式添加%s
    insert_oracle_mysql = "insert into mysql_oracle values (%s,%s,%s)"
    mysql_cursor.execute(insert_oracle_mysql,i)
    mysql_conn.commit()
oracle_cursor.close()
mysql_cursor.close()
mysql_conn.close()
oracle_cursor.close()
