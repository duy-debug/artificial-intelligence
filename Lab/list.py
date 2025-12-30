import math
# tao list rong
emptyList = []
# tao ra mot doi tuong List
emptyList2 = list()
print(emptyList)
print(emptyList2)
# tao ra list co du lieu
colors = ["red", "green", "blue", "yellow", "black"]
print(colors)
studentList = ["An", "Duy", "Hoang", "Khanh", "Linh"]
# list co thu tu, vi tri cac phan tu duoc danh dau tu 0, tu trai sang phai
print(studentList[0])  # An
print(studentList[1])  # Duy
print(studentList[1:2]) # Duy lay ra tu vi tri 1 den 2 (khong bao gom 2)
print(studentList[0:2]) # An, Duy lay ra tu vi tri 0 den 2 (khong bao gom 2)

# them phan tu vao list
studentList.append("Nam")  # Them Nam vao cuoi danh sach
print(studentList)

# chen phan tu vao list
studentList.insert(2, "Hanh")  # Chen Hanh vao vi tri 2
print(studentList)

# xoa phan tu trong list
studentList.remove("Hanh")  # Xoa Hanh khoi danh sach
print(studentList)
# So luong phan tu co trong list: => len
print(len(studentList)) # 6 phan tu

# Dem so luong phan tu thoa dieu kien trong list
print("Dem Ngoc: ", studentList.count("Ngoc"))
print("Dem Thanh: ", studentList.count("Thanh"))
print("Dem An: ", studentList.count("An"))  
# Xoa phan tu ra khoi list bang vi tri 
studentList.pop(2) # Xoa phan tu o vi tri 2
print(studentList)  # Hanh da bi xoa khoi danh sach

# dao nguoc thu tu cua list
studentList.reverse()  # Dao nguoc thu tu cua danh sach 
print(studentList)  # ['Nam', 'Khanh', 'Hoang', 'Duy', 'An']

# Sap xep thu tu cua list

studentList.sort()  # Sap xep thu tu cua danh sach
print(studentList)  # ['An', 'Duy', 'Hoang', 'Khanh', 'Nam']

# Sap xep nguoc
studentList.sort(reverse=True)  # Sap xep nguoc thu tu cua danh sach
print(studentList)  # ['Nam', 'Khanh', 'Hoang', 'Duy', 'An']

# Xoa sach du lieu trong list
studentList.clear()  # Xoa sach du lieu trong danh sach
print(studentList)  # []
