def PlantPumpkin():
	count = 0
	for y in range(get_world_size()):
		for x in range(get_world_size()):
			if get_entity_type() == Entities.Pumpkin:
				count += 1
			if count == get_world_size() ** 2:
				harvest()
			if get_entity_type() != Entities.Pumpkin and not get_entity_type() == None:
				harvest()
				if num_items(Items.Pumpkin_Seed) == 0:
					ItemBuyer(Items.Pumpkin_Seed, get_world_size()**2)
				if get_ground_type() == Grounds.Turf:
					till()
				plant(Entities.Pumpkin)
				WaterSoil()
			else:
				if num_items(Items.Pumpkin_Seed) == 0:
					ItemBuyer(Items.Pumpkin_Seed, get_world_size()**2)
				if get_ground_type() == Grounds.Turf:
					till()
				plant(Entities.Pumpkin)
				WaterSoil()
	
			move(North)
		move(East)