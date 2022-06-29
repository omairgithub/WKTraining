class employee():
    def __init__(self,name,salary,age):
        self.name=name
        self.salary=salary
        self.age=age
    def sal_inc(self):
        self.salary=int(self.salary*1.25)

manager=employee("sam",30000,38)
salesman=employee("joe",20000,30)

salesman.sal_inc()


# manager= employee()
# salesman=employee()
#
# manager.name="Ramesh"
# manager.salary=50000
# manager.age=35
#
# salesman.name="satish"
# salesman.salary=35000
# salesman.age=28

print(salesman.salary)

