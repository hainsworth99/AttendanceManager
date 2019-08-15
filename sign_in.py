#!/usr/bin/env python
# CUCLIMBS sign-in system
# author: Harold Ainsworth, CU Climbing Team, spring 2019
# sign_in.py - driver file for sign-in program
import os
import sys
import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as char_lcd
import datetime as dt
import requests

# base url to be used for all http requests
URL_BASE = 'http://localhost:8000/'


def get_token():
	""" get login token for request authorization use """
	username = os.environ.get('ATTENDANCE_MANAGER_SUPERUSER')
	password = os.environ.get('ATTENDANCE_MANAGER_SUPERUSER_PASSWORD')
	params = {'username': username, 'password': password}
	try:
		response = requests.post(URL_BASE + 'api/rest-auth/login/', json=params)
	except:
		print('Something went wrong, login attempt failed.')
		return None
	return response.json()['key']



def record_attendance(lcd, student_data, token):
	""" records student practice attendence for the current date """



	print('Logging attendance to database...', end=' ')


	lcd.clear()
	lcd.message = '{}\nThank You!'.format(student_data[1])
	print('Task completed, databases are up-to-date.')
	time.sleep(2)

def name_from_data(card_data):
	""" parses first/lastname and student id from card_data """
	# data stored in following format:
	# %B[CARDNUMBER]=[STUDENTID]=[FIRSTNAME/LASTNAME]=[???]?;[CARDNUMBER]=[???]?
	# where both [???] are some unkown number

	# return None if error reading card or card_data formatted incorrectly
	if card_data[1] != 'B' or card_data.count('=') != 4:
		return None

	# split data into fields delimited by '='
	fields = card_data.split('=')
	# [STUDENTID] is second field
	# [FIRSTNAME/LASTNAME] is third field
	sid = fields[1]
	first_last_name = fields[2]
	# replace '/'with ' 'in first/last name
	first_last_name = first_last_name.replace('/', ' ')
	# convert to tuple and return
	return (sid, first_last_name)


def main():
	# LCD pin config
	lcd_rs = digitalio.DigitalInOut(board.D26)
	lcd_en = digitalio.DigitalInOut(board.D19)
	lcd_d7 = digitalio.DigitalInOut(board.D27)
	lcd_d6 = digitalio.DigitalInOut(board.D22)
	lcd_d5 = digitalio.DigitalInOut(board.D24)
	lcd_d4 = digitalio.DigitalInOut(board.D25)
	lcd_backlight = digitalio.DigitalInOut(board.D13)

	# LCD size
	lcd_columns = 16
	lcd_rows = 2

	# LCD class init
	lcd = char_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5,
		 lcd_d6, lcd_d7, lcd_columns, lcd_rows)

	# login and get user token
	token = get_token()

	# main program loop
	while True:
		# get data from card reader
		print('-'*60)
		lcd.clear()
		lcd.message = 'Please swipe\nBuffOne...'
		card_data = input('Please swipe card.\n')
		if card_data == "":
			# for debugging purposes, stop program if enter pressed
			print('Exiting...')
			lcd.clear()
			sys.exit()
		print('Processing...')
		student_data = name_from_data(card_data)

		# ensure data read from card properly
		if student_data is not None:
			# if success...
			record_attendance(lcd, student_data, token)
		else:
			# if error
			lcd.clear()
			lcd.message = 'Error, please\ntry again.'
			print('Error, try again.')
			time.sleep(1.5)


if __name__ == '__main__':
	main()
