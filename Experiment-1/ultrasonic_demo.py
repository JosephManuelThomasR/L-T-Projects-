from machine import Pin, I2C
from time import sleep, sleep_us, ticks_us
import sys
from pico_i2c_lcd import I2cLcd   

TRIG = Pin(16, Pin.OUT)
ECHO = Pin(17, Pin.IN)
LED = Pin(18, Pin.OUT)

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
devices = i2c.scan()

if len(devices) == 0:
    print("No I2C device found!")
    sys.exit()
else:
    I2C_ADDR = devices[0]  # Auto-detect first device (commonly 0x27 or 0x3F)
    print("I2C device found at address:", hex(I2C_ADDR))

lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

def measure_distance():
    TRIG.low()
    sleep_us(2)
    TRIG.high()
    sleep_us(10)
    TRIG.low()
    
    while ECHO.value() == 0:
        start = ticks_us()
    while ECHO.value() == 1:
        end = ticks_us()
    
    duration = end - start
    distance = (duration * 0.0343) / 2  # cm
    return distance

threshold = 20  # cm

lcd.putstr("Ultrasonic Demo\nStarting...")
sleep(2)
lcd.clear()

while True:
    try:
        dist = measure_distance()
        lcd.clear()
        lcd.putstr("Distance:{:.1f}cm".format(dist))
        
        if dist < threshold:
            LED.high()
            lcd.move_to(0, 1)
            lcd.putstr("ALERT! Too Close")
        else:
            LED.low()
            lcd.move_to(0, 1)
            lcd.putstr("Safe Distance")
        
        sleep(1)

    except KeyboardInterrupt:
        lcd.clear()
        lcd.putstr("Program Stopped")
        sys.exit()
