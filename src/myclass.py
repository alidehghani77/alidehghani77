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

