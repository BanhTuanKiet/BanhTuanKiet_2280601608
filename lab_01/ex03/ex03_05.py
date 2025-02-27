def Count(lst):
    countDict = {}
    
    for item in lst:
        if item in countDict:
            countDict[item] += 1
        else:
            countDict[item] = 1
    
    return countDict

inputList = input("Nhap danh sach cac tu cach nhau = dau cach: ")
wordList = inputList.split(' ')

print(Count(wordList))