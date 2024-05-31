def PlantCarrot():
	if num_items(Items.Carrot_Seed) == 0:
		ItemBuyer(Items.Carrot_Seed, get_world_size()**2)
	if get_ground_type() == Grounds.Turf:
		till()
	if can_harvest():
		harvest()
	plant(Entities.Carrots)
	WaterSoil()
	
