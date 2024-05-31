def SortCactus():
	running = True

	while running:
		xList = []
		yList = []
		for y in range(get_world_size()):
			for x in range(get_world_size()):
								
				if measure() > measure(North) and not get_pos_y() == get_world_size() - 1:
					swap(North)
					yList.append(measure())
					quick_print(yList)
					
				if measure() > measure(East) and not get_pos_x() == get_world_size() - 1:
					swap(East)
					xList.append(measure())
								
				move(North)
			move(East)
		if not yList and not xList:
			harvest()
			running = False


def PlantCactus():
	clear()
	for y in range(get_world_size()):
		for x in range(get_world_size()):
			if num_items(Items.Cactus_Seed) == 0:
				trade(Items.Cactus_Seed)
			if get_ground_type() == Grounds.Turf:
				till()
			plant(Entities.Cactus)
			WaterSoil()

			move(North)
		move(East)
	SortCactus()

