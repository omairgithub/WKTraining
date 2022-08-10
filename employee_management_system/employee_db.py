import mysql.connector as a
con=a.connect(host="localhost", user="root",
              passwd="1234", database="wk")

sql="""create table personal
(dob varchar(10),
address varchar(30),
contact_no varchar(10))"""

c=con.cursor()
c.execute(sql)




"""create table official
(emp_id varchar(10),
name varchar(30),
post varchar(20),
joining_date varchar(10),
basic_pay integer)"""