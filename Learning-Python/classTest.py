class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, nam):
        self.name  = nam
        print(self.name, 'constructed')

    def party(self):
        self.x=self.x+1
        print(self.name, 'party count', self.x)

# constructs the person
s = PartyAnimal('Sally')
# creates the count
s.party()


t = PartyAnimal('Tina')
t.party()
t.party()
s.party()
print('---------')


# inheritance -- class with all capabilities of the main class but extended
# also includes extra methods from main class (sample below)

class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points = self.points + 7
        print(self.name, 'points' ,self.points)

k = FootballFan('Kamran')
k.party()
k.touchdown()
k.touchdown()
