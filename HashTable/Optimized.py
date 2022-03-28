
#กรณีนี้ 
#t['march 1'] , t['march 6'] hasdfunction แล้วได้ index เดียวกัน index = 9 


class HashTable:
  def __init__(self):
    self.MAX = 100
    self.arr = [None for i in range(self.MAX)]
  def get_hash(self, key):
    h = 0
    for char in key:
      h += ord(char)
      return h% self.MAX
#กำหนดค่า
  def __setitem__(self, key, val):
    h = self.get_hash(key)
    #ตำแหน่งที่จะนำ item มาใส่ 
    self.arr[h] = val

#ดึงitem
  def __getitem__(self, key):
    h = self.get_hash(key)
    print("index: ", h)
    return self.arr[h]

  def __delitem__(self, key):
    h = self.get_hash(key)
    self.arr[h] = None

t = HashTable()
t['march 6'] = 130
t['march 6']
t['march 1'] = 20
t['march 1'] 



t['dec 17'] = 27
t['dec 17']

print(t.arr) 
del t['march 1']
print(t.arr) 

#The Python del keyword is used to delete objects. Its syntax is:
#del t['march 6']