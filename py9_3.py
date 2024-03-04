import RPi.GPIO as GPIO

from flask import Flask, render_template, request
 
LED1 = 7

LED2 = 11
 
GPIO.setmode(GPIO.BOARD)

GPIO.setup(LED1, GPIO.OUT)

GPIO.setup(LED2, GPIO.OUT)
 
app = Flask(__name__)
 
@app.route("/")

def hello():

    return render_template('meaw.html')
 
@app.route("/led1on", methods=['POST'])

def led1on():

    GPIO.output(LED1, True)

    return "LED1 is on"
 
@app.route("/led1off", methods=['POST'])

def led1off():

    GPIO.output(LED1, False)

    return "LED1 is off"
 
@app.route("/led2on", methods=['POST'])

def led2on():

    GPIO.output(LED2, True)

    return "LED2 is on"
 
@app.route("/led2off", methods=['POST'])

def led2off():

    GPIO.output(LED2, False)

    return "LED2 is off"
 
if __name__ == "__main__":

    app.run(debug=True, host='0.0.0.0')
