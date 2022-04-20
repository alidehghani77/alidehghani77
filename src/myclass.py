import random
from locale import normalize
from re import T


class myClass:
   class_attribute = 99

   def class_method(self):
      self.instance_attribute = 'I am instance attribute'

print (myClass.__dict__)


a= myClass()
a.class_method()
print(a.__dict__)

print(len(['hello', 9 , 45.0, 24]))

#
set1 = {1,2,3,4}
print(set1.__len__())


#
normal_list = [2, 4, 5, 7, 9]

class CustomSequence():
   def __len__(self):
      return 5
   def __getitem__(self,index):
      return "x{0}".format(index)
class funkyback():
    def __reversed__(self):
       return 'backwards!'
  
for seq in normal_list, CustomSequence(), funkyback():
      print('\n{}: '.format(seq.__class__.__name__), end="")
      for item in reversed(seq):
         print(item, end=", ")


# enumerate
names = ['Rajesh', 'Rahul', 'Aarav', 'Sahil', 'Trevor',0]
enumerate(names)
list(enumerate(names))
print("\r")
print(list(enumerate(names)))

for i , n in enumerate(names):
    print('Names number: ' + str(i))
    print(n)
    
#tuple
thistuple = ("apple", "banana", "cherry")
for n in thistuple:
    print(n)
    
# any , all
print("####*******************\r\nexample of any and all built-in function")
print(any(names))
print(all(names))

#open
text = 'This is the first line'
file = open('datawork','w')
file.write(text)
file.close()

#
class Human:
   def sayHello(self, name = None):
      if name is not None:
         print('Hello ' + name)
      else:
         print('Hello ')

#Create Instance
obj = Human()

#Call the method, else part will be executed
obj.sayHello()

#Call the method with a parameter, if part will be executed
obj.sayHello('Rahul')

#
# comment for error use must uncomment it
# def my_func():
#    print('My function was called')
# my_func.description = 'A silly function'
# my_func.test='sad'
# def second_func():

#    print('Second function was called')

#    second_func.description = 'One more sillier function'

# def another_func(func):
#    print("The description:", end=" ")
#    print(func.description)
#    print('The name: ', end=' ')
#    print(func.__name__)
#    print('The class:', end=' ')
#    print(func.__class__)
#    print("Now I'll call the function passed in")
#    func()

# another_func(my_func)
# another_func(second_func)

# __call__
class Example:
    def __init__(self):
        print("Instance Created")

    # Defining __call__ method
    def __call__(self):
        print("Instance is called via special method")

# Instance created
e = Example()

# __call__ method will be called
e()

# inheritance
class Animal(object):
    def __init__(self,name):
        self.name = name
        
    def cat(self,food):
        print("%s is eating %s.%(self.name,food)")
        
class dog(Animal):
    def __init__(self,name):
        super(dog,self).__init__(name)
        self.breed=random.choice(["object1","object2","object3"])
        
    def fetch(self,thing):
        print("%s goes after the! %s.%(self.name,thing)")
    def show_affection(self):
        print("{} whas name.",self.name)
        
class cat(Animal):
    def swatstring(self):
       print("%s shred the string! .%(self.name)") 
    def show_affection(self):
        print("{} whas name***.",self.name)
       
d = dog("Ranger")
c= cat("meow")

d.fetch("ball")
c.swatstring()
d.cat("dog food") 
c.cat("cat food")
d.show_affection()
c.show_affection()

print(d.name)
print(d.breed)
#d.swatstring()    '''error generate'''   

# overriding
class Thought(object):
   def __init__(self):
      pass
   def message(self):
      print("Thought, always come and go")

class Advice(Thought):
    def __init__(self):
      super(Advice, self).__init__()
    def message(self):
      print('Warning: Risk is always involved when you are dealing with market!')
   
    def staticFunc():
        print("Static Func")
        
        
    @classmethod
    def cfunc(cls):
        print("class method")
        

        
      
Advice.staticFunc()
th = Thought()
th.message()
ad = Advice()
ad.message()

#Python Multiple Inheritance Syntax
class Mother:
   pass

class Father:
   pass

class Child(Mother, Father):
   pass

print(issubclass(Child, Mother) and issubclass(Child, Father))
    

