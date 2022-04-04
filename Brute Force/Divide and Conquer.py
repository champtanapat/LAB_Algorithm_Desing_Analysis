# ใช้หลักการ ‘แยก’ ปัญหาเป็น 2 ส่วน
# ส่วนที่ 1 : แบ่งปัญหาออกเป็นส่วนเล็กๆ แล้วแก้ปัญหาส่วนเล็กๆนั้นก่อน
# ส่วนที่ 2 : นำผลที่ได้จากส่วนที่ 1 กลับมารวมกันใหม่

def powerDC(a, n):
    if(n == 0):
        return 1
        
    product = 1 
    while(n): 
        if(n%2):  
            product = product * a  
            a = a * a 
            n = n//2 
    return product

print(powerDC(2,0)) 
print(powerDC(2,3)) 
print(powerDC(2,10)) 