#!/usr/bin/env python3

import rospy
import RPi.GPIO as GPIO
import time

from std_msgs.msg import Int32

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO_Nbr = 11

GPIO.setup(11, GPIO.IN)
GPIO.setup ( 18, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
pi = GPIO.PWM ( 18, 70 )
pi.start(50)

num_keep = 0
r = 0

def callback(num):
	global num_keep
	num_keep = num.data

def keep(duty):
        pi.ChangeDutyCycle(duty)

def stop():
	pi.ChangeDutyCycle(1)

def led():
	GPIO.output(5,1)
	time.sleep(0.1)
	GPIO.output(9,1)
	time.sleep(0.1)
	GPIO.output(10,1)
	time.sleep(0.1)
	GPIO.output(22,1)
	time.sleep(0.1)
	GPIO.output(27,1)
	time.sleep(0.1)
	GPIO.output(17,1)
	time.sleep(0.5)
	GPIO.output(5,0)
	time.sleep(0.1)
	GPIO.output(9,0)
	time.sleep(0.1)
	GPIO.output(10,0)
	time.sleep(0.1)
	GPIO.output(22,0)
	time.sleep(0.1)
	GPIO.output(27,0)
	time.sleep(0.1)
	GPIO.output(17,0)
	time.sleep(0.5)

def wait():
	GPIO.output(3,1)
	r = 0
	while r < 5:
		led()
		r += 1
	GPIO.output(3,0)

try:

	pi.ChangeDutyCycle(0)
	while True:
		if (GPIO.input(11) == 1):
			rospy.init_node('output')
			sub = rospy.Subscriber('Decision_push', Int32, callback)
			keep(num_keep)
			wait()

		else:
			stop()
	rospy.spin()

	Servo.stop()
	GPIO.cleanup()

except rospy.ROSInterruptException: pass
