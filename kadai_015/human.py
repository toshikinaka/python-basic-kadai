class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printinfo(self):
        print(self.name)
        print(self.age)


human = Human("侍太郎", 36)

human.printinfo()