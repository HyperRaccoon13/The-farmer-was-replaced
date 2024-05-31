def DoMaze():
	directions = [North, West, South, East]
	currentDirection = 0
	while get_entity_type() != Entities.Treasure:
		
		while not move(directions[currentDirection]):
			currentDirection += 1
			if currentDirection == 4:
				currentDirection = 0
		currentDirection -= 1
		if currentDirection == -1:
			currentDirection = 3
	
	while get_entity_type() == Entities.Treasure:
		harvest()
	
def MakeMaze():
	if get_entity_type() != Entities.Hedge or Entities.Treasure:
		harvest()
		plant(Entities.Bush)
		while get_entity_type() != Entities.Hedge:
			if num_items(Items.Fertilizer) == 0:
				trade(Items.Fertilizer)	
			use_item(Items.Fertilizer)
		DoMaze()