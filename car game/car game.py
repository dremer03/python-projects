import pygame as pg

pg.init()

Window_size = (1200, 400)
window = pg.display.set_mode(Window_size)
track = pg.image.load('track.png')
car = pg.image.load('tesla.png')
car = pg.transform.scale(car, (30, 60))
BACKGROUND = (0, 255, 0)

car_x = 155
car_y = 300
focal_dis = 25
cam_x_offset = 0
cam_y_offset = 0
direction = "up"
drive = True
clock = pg.time.Clock()
FPS = 60


while drive:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            drive = False
    clock.tick(FPS)

    cam_x = car_x + cam_x_offset + 15
    cam_y = car_y + cam_y_offset + 15
    up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
    right_px = window.get_at((cam_x + focal_dis, cam_y))[0]

    print(up_px, right_px, down_px)

    if direction == "up" and up_px != 255 and right_px == 255:
        direction = "right"
        cam_x_offset = 30
        car = pg.transform.rotate(car, -90)

    elif direction == "right" and right_px != 255 and down_px == 255:
        direction = "down"
        car_x = car_x + 30
        cam_x_offset = 0
        cam_y_offset = 30
        car = pg.transform.rotate(car, -90)

    elif direction == "down" and down_px != 255 and right_px == 255:
        direction = "right"
        car_y = car_y + 30
        cam_x_offset = 30
        cam_y_offset = 0
        car = pg.transform.rotate(car, 90)

    elif direction == "right" and right_px != 255 and up_px == 255:
        direction = "up"
        car_x = car_x + 30
        cam_x_offset = 0
        car = pg.transform.rotate(car, 90)

    if direction == "up" and up_px == 255:
        car_y = car_y - 2

    elif direction == "right" and right_px == 255:
        car_x = car_x + 2

    elif direction == "down" and down_px == 255:
        car_y = car_y + 2

    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y))
    pg.draw.circle(window, BACKGROUND, (cam_x, cam_y), 5, 5)
    pg.display.update()
