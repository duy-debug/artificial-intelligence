# Nhap du lieuj
import math
print("Giai phuong trinh bac 2: ax^2 + bx + c = 0")
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))
# Tinh delta
if a!=0:
    delta = b**2 - 4*a*c
    if(delta<0):
        print("Phuong trinh vo nghiem")
    elif(delta==0):
        x = -b / (2 * a)
        print("Phuong trinh co nghiem kep: x = {0}".format(x))
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Phuong trinh co 2 nghiem phan biet x1 = {0} va x2 = {1}".format(x1, x2))

else:
    print("Khong phai phuong trinh bac 2")