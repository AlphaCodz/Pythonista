x = 25

def my_func():
    x = 50
    return x

print(x)
print(my_func())

# LOCAL
lambda x:x**2

#Enclosing function locals
name = 'This is a global name!'

def greet():
    name = 'Sammy'
    
    def Hello():
        print('Hello ' + name)
        
    Hello()
        
greet()


from tkinter import Y


x = 50

def func(x):
    print('x is: ', x)
    
    x = 1000
    print('local x changed to: ', x)
    
func(x)

y = 20
def move(y):
    y = 1000
    return y
        
print("Before function call, y is: ", y)
move(y)
print("After function call, y is: ", y)
    
                