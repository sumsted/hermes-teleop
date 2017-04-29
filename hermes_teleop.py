import pygame
from hermes_client import *

dragon = True
pygame.init()

last_direction = 'stop'
last_speed = 0

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()

while not done:
    pygame.event.get()

    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    left_right_axis = joystick.get_axis(0)
    fwd_bwd_axis = joystick.get_axis(1)
    speed_axis = joystick.get_axis(5)
    direction_threshold = .8
    max_axis = 1.0
    left_rot_button = joystick.get_button(2)
    right_rot_button = joystick.get_button(3)
    stop_button = joystick.get_button(12)
    quit_button = joystick.get_button(10)

    # axis 0  -1 left 1 right
    # axis 1  -1 up 1 down
    # axis 5  -1 stop 1 go

    print("left_right_axis: %f, fwd_bwd_axis: %f, speed_axis: %f, stop_button: %f" %
          (left_right_axis, fwd_bwd_axis, speed_axis, stop_button))

    speed = 0
    turn = 0

    if fwd_bwd_axis < -direction_threshold or fwd_bwd_axis > direction_threshold:
        speed = -int(100 * (fwd_bwd_axis/max_axis))
    if left_right_axis < -direction_threshold or left_right_axis > direction_threshold:
        turn = int(100 * (left_right_axis/max_axis))

    Hermes_move(speed, turn)

    clock.tick(20)

pygame.quit()
