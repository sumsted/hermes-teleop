import pygame
from hermes_client import *

"""
Hermes-Teleop
Capture joystick input and send to hermes server.

xbox controller mapping

  tf 8             tf 9
  bf 4a            bf 5a
  
   1a                14
 0a +              13  12
                     11
      0         3a
     2 3      2a +
      1
      
"""
PRIMARY_JOYSTICK = 0
LEFT_TOP_FINGER_BUTTON = 8
LEFT_BOTTOM_FINGER_AXIS = 4
RIGHT_TOP_FINGER_BUTTON = 9
RIGHT_BOTTOM_FINGER_AXIS = 5
LEFT_HAT_VERTICAL_AXIS = 1
LEFT_HAT_HORIZONTAL_AXIS = 0
A_BUTTON = 11
B_BUTTON = 12
X_BUTTON = 13
Y_BUTTON = 14
UP_BUTTON = 0
DOWN_BUTTON = 1
LEFT_BUTTON = 2
RIGHT_BUTTON = 3
RIGHT_HAT_VERTICAL_AXIS = 3
RIGHT_HAT_HORIZONTAL_AXIS =2
DIRECTION_THRESHOLD = .2
MAX_AXIS = 1.0

recorded_steps = []
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

    joystick = pygame.joystick.Joystick(PRIMARY_JOYSTICK)
    joystick.init()

    left_right_axis = joystick.get_axis(LEFT_HAT_HORIZONTAL_AXIS)
    fwd_bwd_axis = joystick.get_axis(LEFT_HAT_VERTICAL_AXIS)
    speed_axis = joystick.get_axis(RIGHT_BOTTOM_FINGER_AXIS)
    record_axis = joystick.get_axis(LEFT_BOTTOM_FINGER_AXIS)
    playback_button = joystick.get_button(A_BUTTON)
    erase_button = joystick.get_button(LEFT_TOP_FINGER_BUTTON)

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

    if fwd_bwd_axis < -DIRECTION_THRESHOLD or fwd_bwd_axis > DIRECTION_THRESHOLD:
        speed = -int(100 * (fwd_bwd_axis / MAX_AXIS))
    if left_right_axis < -DIRECTION_THRESHOLD or left_right_axis > DIRECTION_THRESHOLD:
        turn = int(20 * (left_right_axis / MAX_AXIS))

    # if record button held down
    if record_axis > .3:
        recorded_steps.append((speed, turn))

    # playback
    if playback_button > 0:
        for step in recorded_steps:
            Hermes_move(step[0], step[1])
            clock.tick(20)

    # erase
    if erase_button > 0:
        recorded_steps = []

    Hermes_move(speed, turn)

    clock.tick(20)

pygame.quit()
