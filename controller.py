#import evdev
from evdev import InputDevice, categorize, ecodes

# creates object gamepad
gamepad = InputDevice('/dev/input/event1')

# prints out device info at start
print(gamepad)

#  display codes
for event in gamepad.read_loop():
    # buttons 
    if event.type == ecodes.EV_KEY:
        print(event)
    # Analog gamepad
    elif event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        print ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value