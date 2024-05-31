def PlantHay():
	if get_ground_type() == Grounds.Soil:
		till()
	if can_harvest():
		harvest()
	plant(Entities.Grass)
	WaterSoil()