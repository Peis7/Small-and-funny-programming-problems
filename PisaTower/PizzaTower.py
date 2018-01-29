
import time
'''
Here is the thing, create a function that given a in value, will draw(in console)
the 'pisa tower' or at least something that looks like this. The function should
recive as parameter  a char thet will be draw the shape.

 -> if the given value is 1 the result is: *

 -> if the given value is 2 the result is: **
 									      **

-> if the given value is 3 the result is: ***
								  		 * *
										***

-> if the given value is 5, we should get:  *****
										   *   *
									      *   *
									     *   *
									    *****
'''
#1
def pisaTower(n,brickCharacter):
	if n==1:
		return "*"
	print((n-1)*" "+n*str(brickCharacter))
	spaces = n-2
	middleRow = str(brickCharacter)+(n-2)*" "+str(brickCharacter)
	for i in range(n-1,1,-1):
		print(spaces*" " + middleRow)
		spaces = spaces-1
	print(str(n*str(brickCharacter)))

start_time = time.time()
print "start"
pisaTower(10,".")
pisaTower(25,"*")
print "end"
print("--- %s seconds ---" % (time.time() - start_time))


#2.Saving each "row" of the tower in an array.
def pisaTowerRowByRow(n,brickCharacter):
	if n==1:
		return "*"
	result = []
	result.append((n-1)*" "+n*str(brickCharacter))
	spaces = n-2
	middleRow = str(brickCharacter)+(n-2)*" "+str(brickCharacter)
	for i in range(n-1,1,-1):
		result.append(spaces*" " + middleRow)
		spaces = spaces-1
	result.append(str(n*str(brickCharacter)))
	return result
towerRows = pisaTowerRowByRow(100,".")

print("--- %s seconds ---" % (time.time() - start_time))
