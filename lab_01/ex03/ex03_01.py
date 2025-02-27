def tinhTongSoChan(lst):
    tong = 0
    
    for num in lst:
        if (num % 2 == 0):
            tong += num
    
    return tong

inputList = input("Nhap danh sach cac so cach nhau = ',': ")
numbers = list(map(int, inputList.split(',')))

tong = tinhTongSoChan(numbers)

print("Tong cac so chan trong list: ", tong)