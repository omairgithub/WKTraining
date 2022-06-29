class Student:
    def __init__(self,name, email, marks):
        self.name=name
        self.email=email
        self.marks=marks

    # def grade(self):
    #     if self.marks>75:
    #         grade=A
    #     else:
    #         return 2

std1=Student("omair", "omair@gmail", 75)
std2=Student("akash","akash@gmail", 80)



print(std1.__dict__)