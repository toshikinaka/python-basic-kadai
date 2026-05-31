class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age >= 20:
            print(self.name + "は大人です")
        else:
            print(self.name + "は大人ではありません")


human1 = Human("侍太郎", 36)
human2 = Human("侍花子", 18)
human3 = Human("侍次郎", 25)

humans = [human1, human2, human3]

for human in humans:
    human.check_adult()