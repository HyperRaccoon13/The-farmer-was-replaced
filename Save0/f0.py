
itemsDic = [{"Item": Items.Hay, "Min": 100000, "Max": 100},
			{"Item": Items.Wood, "Min": 100000, "Max": 100},
			{"Item": Items.Carrot, "Min": 100000, "Max": 100},
			{"Item": Items.Pumpkin, "Min": 100000, "Max": 100},
			{"Item": Items.Power, "Min": 100000, "Max": 100},
			{"Item": Items.Gold, "Min": 100000, "Max": 100}]

while True:
	for item in itemsDic:
		if item["Item"] == Items.Hay and num_items(Items.Hay) < item["Min"]:
			PlantHay()
			MoveLoop()
		
		elif item["Item"] == Items.Wood and num_items(Items.Wood) < item["Min"]:
			PlantTree()
		
		elif item["Item"] == Items.Carrot and num_items(Items.Carrot) < item["Min"]:
			PlantCarrot()
			MoveLoop()
			
		elif item["Item"] == Items.Pumpkin and num_items(Items.Pumpkin) < item["Min"]:
			PlantPumpkin()
			
		elif item["Item"] == Items.Power and num_items(Items.Power) < item["Min"]:
			PlantSunflower()
			
		elif item["Item"] == Items.Gold and num_items(Items.Gold) < item["Min"]:
			MakeMaze()
	