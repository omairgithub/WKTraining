class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print(self.cpu, self.ram)

    def compare(self,other):
        if self.ram == other.ram:
            return True
        else:
            return False


comp1 = Computer("i3", 13)
comp2 = Computer("i5", 13)
comp1.config()


if comp1.compare(comp2):
    print("They are same")
else:
    print("They are not same")
