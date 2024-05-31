def WaterSoil():
	if get_water() < 0.5:
		use_item(Items.Water_Tank)
		use_item(Items.Water_Tank)