import mysql.connector as a
con=a.connect(host="localhost", user="root",
              passwd="1234", database="wk")

def personal():
    a=input("Enter address of employee")
    d=input("Enter D.O.B of employee")
    c=input("Enter employee's contact no.")
    data=(a,d,c)
    sql='insert into personal values (%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data entered successfully")
    main()

def showPersonal():
    sql="select * from personal"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print(i)
    main()

def official():
    sql="inset into official values(%s,%s,%s,%s,%d)"


def main():
   pass
        