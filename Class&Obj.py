# this is a class

class hack:

    # these are properties

    name = ""
    occ = ""
    age = ""
    games = ""


    def info(self):
        print(f"{self.name} is a {self.occ}. {self.name} is {self.age} years old. {self.name} plays {self.games}")


a = hack()  # this is an object
a.name = "Sajib"
a.occ = "student"
a.age = "20"
a.games = "RDR2"
a.info()

b = hack()
b.name = "Ayon"
b.occ = "student"
b.age = "20"
b.games = "Minecraft"
b.info()

c = hack()
c.name = "Nadman"
c.occ = "student"
c.age = "20"
c.games = "Valorant"
c.info()



