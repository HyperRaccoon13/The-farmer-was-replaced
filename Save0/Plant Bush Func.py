def PlantBush():
	if can_harvest():
		harvest()
	plant(Entities.Bush)
	WaterSoil()