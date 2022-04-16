class Book():
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
        #Return strong Representation
    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author,self.pages)
    
    def __len__(self):
        pass
        
    def __del__(self):
        print('a book is destroyed')

b = Book("Foo Bool", "John Perry", 340)
del b

# Variable B is now deleted so it will throw an undefined error
print(b)