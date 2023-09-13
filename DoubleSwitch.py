import machine
import utime

"""
red - 15
yellow - 14 
green - 13 
blue - 12
button - 11

"""

# setup I/O pins 
red_led = machine.Pin(15, machine.Pin.OUT)
yellow_led = machine.Pin(14, machine.Pin.OUT)
green_led = machine.Pin(13, machine.Pin.OUT)
blue_led = machine.Pin(12, machine.Pin.OUT)
button = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)

counter = 0

def turn_off_lights():
  red_led.value(0)
  yellow_led.value(0)
  green_led.value(0)
  blue_led.value(0)


# loop reads button
while True:
  if button.value() == 1:
    
    counter = counter + 1
    print(f'Counter: {counter}')

    # reset counter
    if counter == 4:
      counter = 0

    if counter == 1:
      turn_off_lights()
      red_led.value(0)
      

    elif counter == 2:
       turn_off_lights()
       yellow_led.value(1)
      

    elif counter == 3:
       turn_off_lights()
       green_led.value(1)
       
    
    else:
       turn_off_lights()
       blue_led.value(1)


    
    utime.sleep(2)

 
  