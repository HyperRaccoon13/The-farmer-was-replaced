maxHay = 10000
maxWood = 10000
maxCarrot = 10000
maxPumpkin = 10000
maxPower = 1000
maxGold = 10000
maxCactus = 10000
maxEgg = 10000

currentMax = 10000
maxNumIncrease = 1000

GoHome()
while True:
	if num_items(Items.Power) < maxPower:
		PlantSunflower()
	
	elif num_items(Items.Hay) < maxHay:
		PlantHay()
		Stepper()
		
	elif num_items(Items.Wood) < maxWood:
		#Plants trees and bushs
		PlantTree()
		#Has own MoveLoop
	
	elif num_items(Items.Carrot) < maxCarrot:
		PlantCarrot()
		Stepper()
	
	
	elif num_items(Items.Pumpkin) < maxPumpkin:
		PlantPumpkin()
		
	elif num_items(Items.Gold) < maxGold:
		MakeMaze()
	
	elif num_items(Items.Cactus) < maxCactus:
		PlantCactus()
		
	elif num_items(Items.Egg) < maxEgg and num_items(Items.Cactus) > 30000:
		Dino()
	else:
		clear()
		maxHay += maxNumIncrease
		maxWood += maxNumIncrease
		maxCarrot += maxNumIncrease
		maxPumpkin += maxNumIncrease
		maxPower += maxNumIncrease
		maxGold += maxNumIncrease
		maxCactus += maxNumIncrease
		maxEgg += maxNumIncrease
		
		currentMax += maxNumIncrease
		quick_print(currentMax)