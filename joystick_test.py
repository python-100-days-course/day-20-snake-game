# # Not used, test code!
#
# import pygame # need to get the package
# pygame.init()
# joysticks = []
# clock = pygame.time.Clock()
# keepPlaying = True
#
# # for al the connected joysticks
# for i in range(0, pygame.joystick.get_count()):
#     # create an Joystick object in our list
#     joysticks.append(pygame.joystick.Joystick(i))
#     # initialize the appended joystick (-1 means last array item)
#     joysticks[-1].init()
#     # print a statement telling what the name of the controller is
#     print ("Detected joystick "),joysticks[-1].get_name(),"'"

from pygame import *

init()
display.init()

#Setup and init joystick
j=joystick.Joystick(0)
j.init()

#Check init status
if j.get_init() == 1: print "Joystick is initialized"

#Setup event information and print data from joystick
while 1:
    for e in event.get():
        if e.type != QUIT:
            print('%s: %s' % (event.event_name(e.type), e.dict))