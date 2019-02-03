import urllib
import requests
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import os

def exists(path):
    r = requests.head(path)
    return r.status_code == requests.codes.ok

website = 'http://files.hearthscry.com/collectobot/'
local_dir = '/home/eduardo/personal_git/HS_samples/Extract/HearthScry/'
first_date = datetime(2016, 6, 1)
date = first_date

while date:
	filename = str(date.year) + '-' + '{:02d}'.format(date.month)  + '.zip'
	filepath =  website + filename
	local_filepath = local_dir + filename
	if exists(filepath):
		print("downloading file: " + filepath)
		response = urllib.urlretrieve(filepath, local_filepath)
		date = date + relativedelta(months=1)
	else:
		print("file " + filename + " does not exist!")
		if date > datetime.today():
			date = None
		else:
			date = date + relativedelta(months=1)

recent_date = datetime.today() - relativedelta(months=1)
recent_date = recent_date.replace(day=1)
while recent_date:
	filename = str(recent_date.year) + '-' + '{:02d}'.format(recent_date.month)  + '-' + '{:02d}'.format(recent_date.day) + '.zip'
	filepath =  website + filename
	local_filepath = local_dir + filename
	if exists(filepath):
		print("downloading file: " + filepath)
		response = urllib.urlretrieve(filepath, local_filepath)
		recent_date = recent_date + timedelta(days=1)
	else:
		print("file " + filename + " does not exist!")
		if recent_date > datetime.today():
			recent_date = None
		else:
			recent_date = recent_date + timedelta(days=1)