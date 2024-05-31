def GoHome():
	for y in range(get_pos_y()):
		move(South)
	for x in range(get_pos_x()):
		move(West)
