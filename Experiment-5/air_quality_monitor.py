from machine import Pin, ADC, I2C
import ssd1306
import time
mq135 = ADC(Pin(26))
buzzer = Pin(15, Pin.OUT)
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)
THRESHOLD = 180
def get_ppm(value):
    return int((value / 65535) * 1000)

while True:
    raw_value = mq135.read_u16()
    ppm = get_ppm(raw_value)
    oled.fill(0)
    oled.text("Air Quality", 0, 0)
    oled.text("PPM: {}".format(ppm), 0, 20)

    if ppm > THRESHOLD:
        oled.text("Status: BAD", 0, 40)
        buzzer.value(1)
    else:
        oled.text("Status: GOOD", 0, 40)
        buzzer.value(0)
    oled.show()
    print("Raw:", raw_value, " PPM:", ppm)
    time.sleep(1)
