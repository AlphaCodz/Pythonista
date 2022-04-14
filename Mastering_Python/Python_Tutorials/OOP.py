# mylist = [1 , 2, 3]
# mylist.append(4)
# print(mylist)

# print(type(mylist)) #List
# print(type(())) #Tuple
# print(type({})) #Dictionary

# class Sample():
#     pass

# x = Sample()
# print(type(x))

#Attributes are characteristics of an object
#Methods are operations we can perform on an object


# class Dog():
#     #Class object Attributes
#     species = "Mammal"
  
#   #Attributes
#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name = name
 
# mydog = Dog("Lab", "Cherry")
# print(mydog.breed)   
# print(mydog.name)
# print(mydog.species)   


class Circle():
  
  pi = 3.14
  
  def __init__(self, radius = 1):
    self.radius = radius
    
  def area(self):
        #Formula is Area = r2 * pi
        A =  self.radius*self.radius * Circle.pi
        return f"Area = {A}"
      
      #Methods that reset object attribute
  def set_radius(self, new_r):
        self.radius = new_r
        
    
myc = Circle(3)
myc.set_radius(999)
print(myc.area())