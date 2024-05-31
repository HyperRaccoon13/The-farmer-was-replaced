def Goto(xPos, yPos):
	while not get_pos_x() == xPos:
		if xPos < get_pos_x():
			move(West)
		elif xPos > get_pos_x():
			move(East)
	while not get_pos_y() == yPos:
		if yPos < get_pos_y():
			move(South)
		elif yPos > get_pos_y():
			move(North)
