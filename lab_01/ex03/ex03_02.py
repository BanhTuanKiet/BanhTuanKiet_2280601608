def DaoNguocChuoi(chuoi):
    return chuoi[::-1]

inputList = input("Nhap danh sach cac so cach nhau = ',': ")
numbers = list(map(int, inputList.split(',')))

print("Chuoi dao nguoc la: ", DaoNguocChuoi(numbers))