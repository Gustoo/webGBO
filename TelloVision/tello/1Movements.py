from djitellopy import tello
from time import sleep

fly = tello.Tello()
fly.connect()
print(fly.get_battery())
print(fly.get_barometer())
print(fly.get_distance_tof())
print(fly.get_roll())
#get_height() get_yaw() pitch roll
fly.takeoff()
fly.send_rc_control(0,-20,0,0)
sleep(2)
#fly.flip_back()
#fly.rotate_clockwise(90)
fly.land()
