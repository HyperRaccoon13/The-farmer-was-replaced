def Dino():
	running = True
	if num_items(Items.Cactus) >= 60:
		while running:
			list = []
	
			for y in range(get_world_size()):
				for x in range(get_world_size()):
					if num_items(Items.Egg) == 0:
						trade(Items.Egg)
					if measure() != 0:
						harvest()
					use_item(Items.Egg)
					if Entities.Dinosaur:
						list.append(measure())
					
					move(North)
				move(East)
			quick_print(list)
			if GetAverage(list) <= 0.2 and measure() == 0:
				harvest()
				running = False
				clear()
	else:
		harvest()
		clear()
