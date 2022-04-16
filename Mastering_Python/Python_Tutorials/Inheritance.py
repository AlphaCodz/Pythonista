class Animal():
    
    def __init__(self):
        print("Animal Created")
        
    def WhatIsThat(self):
        print("Animal")
        
    def Eat(self):
        print("Animal is Eating")
        
class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
        
        
# animal1 = Animal()
# #These 2 will print without using the print keyword, because their is a print keyword in each of the functions
# animal1.WhatIsThat()
# animal1.Eat()

animal2 = Dog()
animal2.WhatIsThat()