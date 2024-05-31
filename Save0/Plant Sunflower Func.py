
def PlantSunflower():
	clear()
	petals = []
	petalsPos = []
	maxPetal = 0
	for y in range(get_world_size()):
		for x in range(get_world_size()):
			if num_items(Items.Sunflower_Seed) == 0:
				trade(Items.Sunflower_Seed)
			if get_ground_type() == Grounds.Turf:
				till()
			plant(Entities.Sunflower)
			WaterSoil()
			petals.append(measure())
			petalsPos.append((get_pos_x(), get_pos_y()))
			
			move(North)
		move(East)
	maxPetal = max(petals)
	avgPetal = GetAverage(petals)
	if avgPetal <= 9.75:
		clear()

	count = 0
	for petal in petals:
		if petal == maxPetal:
			break
		count += 1
	Goto(petalsPos[count][0], petalsPos[count][1])
	harvest()
