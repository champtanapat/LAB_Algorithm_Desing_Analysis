# Divide and Conquer 
def powerDC_Re(a,n): 
 #Big O(1) 
 if(n == 0): 
   return 1 
#Big O( log n ) 
 if(n%2 == 0): 
                # O(n/2)   + O(n/2) 
   return powerDC_Re(a, n//2) * powerDC_Re(a, n//2)  
 else: 
                # O(n/2)   + O(n/2) 
   return a * powerDC_Re(a, n//2) * powerDC_Re(a, n//2) 
# = O(1) + O ( log n )   + O(n) + O(n) + O(n) + O(n) 
# = O(n) 
# recusive call O(n) 
print(powerDC_Re(2,0)) 
print(powerDC_Re(2,3)) 
print(powerDC_Re(2,10)) 
