class Animel:
    def __init__(self,name):
        self.name = name
        print(f"{self.name} is created")
    def eat(self):
        print(f"{self.name} is eating")
class canfly:
    def __init__(self):
        print(f"{self.name} Can fly")
    def fly(self):
        print(f"{self.name} is flying")
        
class canwalk:
    def __init__(self):
        print(f"{self.name}Can walk")
    def walk(self):
        print(f"{self.name} is walking")
        
class bird(Animel,canfly,canwalk):
    def __init__(self,name):
        Animel.__init__(self,name)
        canfly.__init__(self)
        canwalk.__init__(self)
        print("Bird is created")
        
    def tweet(self):
        print("Bird is tweeting")
        

bird1 = bird("Parrot")
bird1.eat()
bird1.fly()
bird1.walk()
bird1.tweet()
print()
bird2 = bird("Eagle")
bird2.eat()
bird2.fly()
bird2.walk()
bird2.tweet()
print()
bird3 = bird("Sparrow")
bird3.eat()
bird3.fly()
bird3.walk()
bird3.tweet()
print()