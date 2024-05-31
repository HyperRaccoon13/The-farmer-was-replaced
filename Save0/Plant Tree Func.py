
def PlantTree():
	if get_pos_y() == get_world_size() -1:
		if not IsEven(get_pos_y()) and not IsEven(get_pos_x()):
			Harvester()
		PlantBush()
		move(East)
		move(North)
	else:
		if IsEven(get_pos_y()) and IsEven(get_pos_x()):
			Harvester()
			move(North)
			
		elif not IsEven(get_pos_y()) and not IsEven(get_pos_x()):
			Harvester()
			move(North)
		else:
			PlantBush()
			move(North)
		 
def Harvester():
	if can_harvest():
		harvest()
	plant(Entities.Tree)
	WaterSoil()

