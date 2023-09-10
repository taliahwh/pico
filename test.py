import machine

# button is connected to GP14, configures it as an input with resistor set to pull-down
# pico includes an on-board programmable resistor connected to each GPIO pin
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)