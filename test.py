import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(32, GPIO.OUT)

t1 = GPIO.PWM(32, 50)

t1.start(0)

t1.ChangeDutyCycle(7.5)
time.sleep(30)

t1.stop()

GPIO.cleanup()
quit()
