def AccessElement(tupple):
    firstEle = tupple[0]
    lastEle = tupple[-1]
    
    return firstEle, lastEle

inputTupple = eval(input("Nhap tupple: "))

first, last = AccessElement(inputTupple)
print("First, Last: ", first, last)