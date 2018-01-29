def binarySearch(set,target):
	setSize = len(set)
	print("set size: "+str(setSize))
	actualIndex = setSize//2
	actualSetLenght = setSize//2
	cont = 0
	while (actualSetLenght > 0 ):
		#print("1. "+str(actualIndex))
		if(set[actualIndex] == target):
			return actualIndex
		left = True if (set[actualIndex] > target) else False
		actualSetLenght = (actualSetLenght//2)+1
		print("actualSetLenght: "+str(actualSetLenght)+"  left: "+str(left))
		before = actualIndex
		actualIndex = actualIndex +  (-1*actualSetLenght if left else actualSetLenght-1)
		print("2. "+str(actualIndex))
		rangel = set[actualIndex:before] if left else set[before:actualIndex]
		print(rangel)
		#print(str(set[actualIndex]))
		cont+=1
	return None
set1 = []
print(3//2)
print(4//2)
for n in range(1,209):
	set1.append(n)
print("start")
print(" ====== n"+str(n))
print(set1)
res = binarySearch(set1,208)
print("end")
print(res)
#1 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200
#2 193, 194, 195, 196, 197, 198, 199, 200
#3 196, 197, 198, 199, 200
#4
#
#
#
#
#
#
#
#


