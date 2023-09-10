import machine
import utime

# setup input/output pins
# blue - 15
# red - 14
#  btn - 11
led_external = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

# loop reads the button
while True:
  if button.value() == 1:
    led_external.value(1)
    print('Lights on!!')
    utime.sleep(2)
  led_external.value(0)