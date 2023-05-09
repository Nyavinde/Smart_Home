from flask import Flask, request, render_template
import RPi.GPIO as GPIO
from time import sleep
from time import sleep
import drivers
from datetime import datetime

#Setting the application
app = Flask(__name__)

Kitchen=22
Bedroom=27
Coupler1=5
Coupler2=6
Fan=14

#  Defining display for lcd
display = drivers.Lcd()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#setting my appliances as output
GPIO.setup(Kitchen, GPIO.OUT)
GPIO.setup(Bedroom, GPIO.OUT)
GPIO.setup(Coupler1, GPIO.OUT)
GPIO.setup(Coupler2, GPIO.OUT)
GPIO.setup(Fan, GPIO.OUT)


display.lcd_display_string(str(datetime.now().now()),2)
display.lcd_display_string("     MY HOME    ",1)


#default url
@app.route('/')

def index():
    GPIO.output(Kitchen, 1)
    GPIO.output(Bedroom, 1)
    GPIO.output(Coupler1, 1)
    GPIO.output(Coupler2, 1)
    GPIO.output(Fan, 1)
    
    return render_template("login.html")
database={'Nyavinde':'12345'}

#Calling and getting the login page
@app.route('/form_login',methods=['POST','GET'])

def login():
    name1=request.form['username'] #Entered name
    psw=request.form['password'] #Entered password

    #Checking and confirming login deatils
    if name1 not in database: 
        return render_template('login.html',info='Invalid user')
    
    else:
        if database[name1]!=psw: 
            return render_template('login.html',info='Invalid Passowrd')

        else:
            return render_template('home.html',name=name1)



@app.route('/kitchen_off')
def kitchen_off():
    GPIO.output(Kitchen,1)
    display.lcd_display_string("  KITCHEN OFF  ",1)
    sleep(2)
    display.lcd_display_string("     MY HOME    ",1)
    return render_template('home.html')


@app.route('/kitchen_on')
def kitchen_on():
    GPIO.output(Kitchen,0)
    display.lcd_display_string("  KITCHEN ON  ",1)
    sleep(2)
    display.lcd_display_string("     MY HOME    ",1)
    return render_template('home.html')


@app.route('/bedroom_off')
def bedroom_off():
    GPIO.output(Bedroom,1)
    display.lcd_display_string("  BEDROOM OFF  ",1)
    sleep(2)
    display.lcd_display_string("     MY HOME    ",1)
    return render_template('home.html')

@app.route('/bedroom_on')
def bedroom_on():
    GPIO.output(Bedroom,0)
    display.lcd_display_string("  BEDROOM ON  ",1)
    sleep(2)
    display.lcd_display_string("     MY HOME    ",1)
    return render_template('home.html')


@app.route('/coupler1_off')
def coupler1_off():
    GPIO.output(Coupler1,1)
    display.lcd_display_string("  HEAD_PLUG1 OFF  ",1)
    sleep(2)
    display.lcd_display_string("     MY HOME    ",1)
    return render_template('home.html')

@app.route('/coupler1_on')
def coupler1_on():
    GPIO.output(Coupler1,0)
    display.lcd_display_string("  HEAD_PLUG1 ON  ",1)
    sleep(2)
    display.lcd_display_string("     MY HOME    ",1)
    return render_template('home.html')
 
@app.route('/fan_off')
def fan_off():
    GPIO.output(Fan,1)
    display.lcd_display_string(" FAN TURNED OFF  ",1)
    sleep(2)
    display.lcd_display_string("     MY HOME    ",1)
    return render_template('home.html')

@app.route('/fan_on')
def fan_on():
    GPIO.output(Fan,0)
    display.lcd_display_string(" FAN TURNED  ON  ",1)
    sleep(2)
    display.lcd_display_string("     MY HOME    ",1)
    return render_template('home.html')


if __name__ == "__main__":
   app.run()
