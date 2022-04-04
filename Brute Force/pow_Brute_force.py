def power(a,n):
#Big O(n) 
 product = 1 
 for i in range(n): 
     product = product * a  
 return product 
 
print(power(2,0)) 
print(power(2,3)) 
print(power(2,10)) 
