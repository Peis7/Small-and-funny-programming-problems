

print("-------------------------------------")
#given an array on numbers and a target number, find it there is a pair of numbers in the array that add up
#to target [1,2,3,4,5,8,12,34,56,78] - 24    , [74,34,24,14,8,7,6,4,2,1]  -  20
#the array is sorted
def findPair(set,target):
	if (len(set) < 2):
		return False
	numbersCount = len(set)
	setTemp = set
	sortOrderDesc = True if setTemp[0] > setTemp[1] else False
	if ((setTemp[len(setTemp)-1] >= target) if sortOrderDesc else (setTemp[0] >= target)):#set is sorted, so if smaller number on set is greater or equal than target, nothing else to do
		return None
	validSmallerNumbers = None
	originalSetActualIndex = 0
	direction = -1 if (setTemp[len(setTemp)/2] < target) else 1
	while (validSmallerNumbers == None):
		left = True if (setTemp[len(setTemp)/2] < target) else False
		print("left = "+str(left)+ "    =   "+str(setTemp))
		originalSetActualIndex = abs(originalSetActualIndex + (-1*len(setTemp)/2 if left else len(setTemp)/2))
		if(setTemp[len(setTemp)/2] >= target and len(setTemp) > 1 and setTemp[(len(setTemp)/2)-1] <= target) or len(setTemp)==1:
			print("eureka")
			validSmallerNumbers = setTemp[len(setTemp)/2]
			setTemp = set[0:numbersCount/2] if not left else set[numbersCount/2:numbersCount]
		else:
			setTemp = setTemp[0:len(setTemp)/2] if left else setTemp[len(setTemp)/2:len(setTemp)]
		print(originalSetActualIndex)
	print(setTemp)
	print(str(validSmallerNumbers)+str(" <= subarray that makes sense to evaluate ----"))

print(findPair([1,2,3,4,5,6,45,65,67,88,98,123,145,178,203,223,245,267,300,456,877],69))


#after finding the sub array that makes sense to evaluate items , then we go evaluate this item against
#all items that are smaller or equal to target - actual_item
#[1,2,3,4,5,6,45,65,67,88,98,123,145,178,203,223,245,267]
#the we use binary search to find if there is target - actual_item in the array, if there is, result would be
#we start looking and if
