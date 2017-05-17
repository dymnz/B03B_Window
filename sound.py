from gtts import gTTS
import os
import datetime
import random

sound_dir = './sound/'

def english(text):
	tts = gTTS(text=text, lang='en')
	tts.save(sound_dir + "speech.mp3")
	os.system("mpg321 " + sound_dir + "speech.mp3")

def chinese(text):
	tts = gTTS(text=text, lang='zh-tw')
	tts.save(sound_dir + "speech.mp3")
	os.system("mpg321 " + sound_dir + "speech.mp3")


def googoogoo():
	os.system("mpg321 " + sound_dir +"googoogoo.mp3")

def glocke():
	os.system("mpg321 " + sound_dir +"glocke.mp3")


def random_fart():
	if random.randint(0,100) == 0:
		os.system("mpg321 " + sound_dir +"fart.mp3")	

def tell_time():
	s = datetime.datetime.now().strftime('%I:%M%p')
	d = s[:2] + s[-2:]
	glocke()
	chinese('現在時間,'+   d )


