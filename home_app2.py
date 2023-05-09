from flask import Flask, request, render_template
import RPi.GPIO as GPIO
from time import sleep


from datetime import datetime

#Setting the application
app = Flask(__name__)

Kitchen=22
Bedroom=27
Coupler1=5
Coupler2=6
Fan=14



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#setting my appliances as output
GPIO.setup(Kitchen, GPIO.OUT)
GPIO.setup(Bedroom, GPIO.OUT)
GPIO.setup(Coupler1, GPIO.OUT)
GPIO.setup(Coupler2, GPIO.OUT)
GPIO.setup(Fan, GPIO.OUT)

#Initializing appliances as low
GPIO.output(Kitchen, 1)
GPIO.output(Bedroom, 1)
GPIO.output(Coupler1, 1)
GPIO.output(Coupler2, 1)
GPIO.output(Fan, 1)

#Initializing for a door sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.IN,pull_up_down=GPIO.PUD_UP)


database={'Nyavinde':'12345'}


#default url
@app.route('/')
def index():
   

    return render_template("login.html")


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
    
    return render_template('home.html')


@app.route('/kitchen_on')
def kitchen_on():
    GPIO.output(Kitchen,0)

    return render_template('home.html')


@app.route('/bedroom_off')
def bedroom_off():
    GPIO.output(Bedroom,1)
    return render_template('home.html')

@app.route('/bedroom_on')
def bedroom_on():
    GPIO.output(Bedroom,0)
    return render_template('home.html')


@app.route('/coupler1_off')
def coupler1_off():
    GPIO.output(Coupler1,1)
    return render_template('home.html')

@app.route('/coupler1_on')
def coupler1_on():
    GPIO.output(Coupler1,0)
    return render_template('home.html')
 
@app.route('/coupler2_off')
def coupler2_off():
    GPIO.output(Coupler2,1)
    return render_template('home.html')

@app.route('/coupler2_on')
def coupler2_on():
    GPIO.output(Coupler2,0)
    return render_template('home.html')
    
@app.route('/fan_off')
def fan_off():
    GPIO.output(Fan,1)
    return render_template('home.html')

@app.route('/fan_on')
def fan_on():
    GPIO.output(Fan,0)
    return render_template('home.html')


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=800, debug=True)
