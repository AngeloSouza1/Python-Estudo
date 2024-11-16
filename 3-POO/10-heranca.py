class Animal:
    name = ""
    size = ""
    color = ""    
    
    def eat(self):
        print("Animal se alimentando")

class Horse(Animal):
    race = ""

    def escape(self):
        print("Cavalo fugindo")

class Lion(Animal):
    mane = ""
    
    def hunt(self):
        print("Leão caçando")
    
h = Horse()
h.name = "Carpeado"
h.color = "branco"
h.escape()
h.eat()

l = Lion()
l.name = "Simba"
l.color = "marron"
l.eat()
l.hunt()