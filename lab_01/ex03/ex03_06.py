def DeleteEle(dic, key):
    if key in dic:
        del dic[key]
        
        return True
    
    return False

myDic = {
    'a': 1,
    'b': 2,
    'c': 3
}

key = input("Nhap key muon xoa: ")

if DeleteEle(myDic, key):
    print(f"Da xoa {key} khoi myDic")
else:
    print(f"Khong tim thay {key} trong myDic")