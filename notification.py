import serial
from sound import *
from temp import *
from apscheduler.schedulers.blocking import BlockingScheduler

def dinner():
		glocke()
		english('Time for dinner!')
		tell_weather()

def lunch():
		glocke()
		english('Time for lunch!')
		tell_weather()

def say_hello():
	for line in ser.read():
		s = datetime.datetime.now().strftime('%H:%M')
		hour = int(s[:2])
		if 6 <= hour < 11:
			english('good morning')
		elif 11 <= hour < 14:
			english('good evening')
		elif 14 <= hour < 18:
			english('good afternoon')
		elif 18 <= hour <= 23 or 0 <= hour < 6:
			english('good night')			
		else:
			english('hello')

scheduler = BlockingScheduler()

# Tell time
scheduler.add_job(tell_time, 'cron', hour='0-23')

# Crowing
scheduler.add_job(googoogoo, 'cron', hour='9,22,23,0-3')

# Food
scheduler.add_job(lunch, trigger='cron', hour='11', minute='40')
scheduler.add_job(dinner, trigger='cron', hour='17', minute='0')

# Random fart
scheduler.add_job(random_fart, 'interval', minutes=10)

# Sound test
glocke()

# test
scheduler.add_job(say_hello, 'interval', seconds=1)

# Start serial
ser = serial.Serial(
	port='/dev/ttyACM0',\
	baudrate=9600,\
	parity=serial.PARITY_NONE,\
	stopbits=serial.STOPBITS_ONE,\
	bytesize=serial.EIGHTBITS,\
		timeout=0)

# Start scheduler
scheduler.start()

ser.close()
