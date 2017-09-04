#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import cx_Oracle, pymysql.cursors

# oracle_conn =cx_Oracle.connect('system/oracle@192.168.1.111:1521/xe')
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'python',
    'charset': 'utf8',
}
config2 = {
    'host': '192.168.1.11',
    'port': 3306,
    'user': 'zhang',
    'password': '123456',
    'db': 'cmdb',
    'charset': 'utf8',
}
oracle_conn = pymysql.connect(**config)
select_sql_mysql = 'select * from app01_business where id <>2'
oracle_cursor = oracle_conn.cursor()
oracle_sql = oracle_cursor.execute(select_sql_mysql)
obj = oracle_cursor.fetchall()
# print obj
mysql_conn = pymysql.connect(**config2)
mysql_cursor = mysql_conn.cursor()
for i in obj:
    insert_oracle_mysql = "insert into mysql_oracle values (%s,%s,%s)"
    mysql_cursor.execute(insert_oracle_mysql,i)
    mysql_conn.commit()
oracle_cursor.close()
mysql_cursor.close()
mysql_conn.close()
oracle_cursor.close()
