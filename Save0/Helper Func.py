def IsEven(number):
	return number % 2 == 0
	
def Mover(direction, numberOfTime):
	for i in range(numberOfTime):
		move(direction)
		
def ItemBuyer(item, count):
	if not trade(item, count):
		trade(item)

def TradeReq(item, req):
	while num_items(item) < req:
		if not trade(item):
			return False
	return True		
	
def GetAverage(numbers):
	if len(numbers) == 0:
		return 0
	
	totalSum = 0
	for n in numbers:
		totalSum += n
	
	count = len(numbers)
	average = totalSum / count
	return average
	
def GetBubbleSort(list):
	listLen = len(list)
	for i in range(listLen):
		for j in range(0, listLen-i-1):
			if list[j] > list[j+1]:
				list[j], list[j+1] = list[j+1], list[j]
	return list

def GetMinMaxSort(list):
	minNum = min(list)
	maxNum = max(list)
	sortedList = list[0] == minNum and list[-1] == maxNum
	return sortedList