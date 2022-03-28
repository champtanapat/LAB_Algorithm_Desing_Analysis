#กรณี  hasd table ชนกัน 
#setitem 
#element[0] = key 
#element[1] = value 

class HashTable:
  def __init__(self):
    self.MAX = 10
    self.arr = [[] for i in range(self.MAX)]
  def get_hash(self, key):
    hash = 0
    for char in key:
      hash += ord(char)
    return hash % self.MAX
  
  def __getitem__(self, idex):
    h = self.get_hash(idex)
    return self.arr[h]
  
  def __setitem__(self, key, val):
    h = self.get_hash(key)
    found = False
    for idx, element in enumerate(self.arr[h]):
      print("element: ",element)
      print("len: ",len(element))
      #element[0] = key 
      #element[1] = value  
      if len(element) == 2 and element[0] == key:
        self.arr[h][idx] = (key, val)
        found = True
        break
    if not found:
      self.arr[h].append((key,val))

t = HashTable()
print(t.get_hash("march 6"))
print(t.get_hash("march 17"))

t["march 6"] = 120
t["march 8"] = 67
t["march 9"] = 4
t["march 17"] = 459
print(t.arr[0]) 
print(t.arr[1]) 
print(t.arr[2]) 
print(t.arr[9]) 
print(t.arr[9][0]) 
print(t.arr[9][1]) 
