import mouse as ms

SPEED = 0.1

x, y = 0, 0

while 1:
    current_x, current_y = ms.get_position()
    x_dist, y_dist = current_x - x, current_y - y
    # print(x_dist, y_dist)

    print(current_x - (x_dist * SPEED), current_y - (y_dist * SPEED))
