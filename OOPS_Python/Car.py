class Car:

    wheels = 4

    def __init__(self):
        self.mile = 10
        self.company = "BMW"


c1 = Car()
c2 = Car()

c1.mile = 8

print(c1.company, c1.mile, c1.wheels)
print(c2.company, c2.mile, c2.wheels)
