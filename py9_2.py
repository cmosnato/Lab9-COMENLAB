
import RPi.GPIO as GPIO

from flask import Flask
 
LED1 = 7

LED2 = 11
 
GPIO.setmode(GPIO.BCM)

GPIO.setup(LED1, GPIO.OUT)

GPIO.setup(LED2, GPIO.OUT)
 
app = Flask(__name__)
 
@app.route('/<opt>/<state>')

def calculate(opt, state):

    if opt == 'led1':

        if state == 'on':

            GPIO.output(LED1, True)

            return 'led1 on'

        elif state == 'off':

            GPIO.output(LED1, False)

            return 'led1 off'

    elif opt == 'led2':

        if state == 'on':

            GPIO.output(LED2, True)

            return 'led2 on'

        elif state == 'off':

            GPIO.output(LED2, False)

            return 'led2 off'

    return 'Invalid request'
 
if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')
