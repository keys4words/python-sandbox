class Character:
    def __init__(self, name):
        self.health = 100
        self.name = name

    def showName(self):
        print(self.name)


class Forge:
    def __init__(self, forgeName):
        self.name = forgeName


class Blacksmith(Character):
    def __init__(self, name, forgeName):
        super().__init__(name)
        self.forge = Forge(forgeName)



bs = Blacksmith('Bob', "Rick's forge")
bs.showName()
# print(bs.health)
print(bs.forge.name)