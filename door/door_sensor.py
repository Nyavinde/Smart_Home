import time, sys
import RPi.GPIO as GPIO
from datetime import datetime
import drivers



GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.IN,pull_up_down=GPIO.PUD_UP)


pre_state=1
display = drivers.Lcd()

display.lcd_display_string("   My Home   ",1)

while True:
    door_closed=GPIO.input(20)
    display.lcd_display_string(str(datetime.now().now()),2)
    if door_closed==True and door_closed!=pre_state:
        print("door open")
        display.lcd_display_string(" Door is opened",1)
        time.sleep(2)
        pre_state=door_closed
        
    elif door_closed==False and door_closed!=pre_state:
        print("door closed")
        display.lcd_display_string(" Door is closed",1)
        time.sleep(2)
        pre_state=door_closed
        
    else:
       #display.lcd_display_string("    MY HOME    ",1)
        display.lcd_display_string("   SMART HOME    ",1)
