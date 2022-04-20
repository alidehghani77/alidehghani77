class InstanceCounter(object):
   count = 0 # class attribute, will be accessible to all instances
   def __init__(self, val):
      self.val = val
      InstanceCounter.count +=1 # Increment the value of class attribute, accessible through class name
# In above line, class ('InstanceCounter') act as an object
   def set_val(self, newval):
      self.val = newval

   def get_val(self):
      return self.val

   def get_count(self):
      return InstanceCounter.count
a = InstanceCounter(9)
b = InstanceCounter(18)
c = InstanceCounter(27)

for obj in (a,b):
   print ('val of obj: %s' %(obj.get_val())) # Initialized value ( 9, 18, 27)
   print ('count: %s' %(obj.get_count())) # always 3