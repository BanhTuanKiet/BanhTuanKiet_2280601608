def CreateTuppleFromList(lst):
        return tuple(lst)
    
inputList = input("Nhap danh sach cac so cach nhau = ',': ")
numbers = list(map(int, inputList.split(',')))
    
myTupple = CreateTuppleFromList(numbers)

print("Tupple: ", myTupple)
