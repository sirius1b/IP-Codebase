#Lavanya Verma
#Roll no.2018155
#Section & Group :A3
import urllib.request
import datetime
# function to get weather response
def weather_response(location, API_key):
	json = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?q='+location+'&APPID='+API_key) #request for json string
	x= str(json.read()) #store json string as string type object
	return (x)
# function to check for valid response 
def has_error(location,json):
	if not location in json:
		return True
	
# function to get attributes on nth day
def get_temperature (json, n=0, t="03:00:00"):
	todaydate=(datetime.date.today()) #store today date as bytes
	adddate=str(todaydate+datetime.timedelta(days=n)) #date want to address
	future=adddate+' '+t #datetime format for finding in json
	indexf=json.find(future) # index of datetime
	end=json.rfind(',"temp_min"',0,indexf) #end index of parameter's required value 
	indext=json.rfind('"temp"',0,indexf) #starting index of parameter's required value
	temp=(json[indext+7:end]) #slicing of json string
	return float(temp)
def get_humidity(json, n=0, t="03:00:00"):
	todaydate=(datetime.date.today()) #store today date as bytes
	then=str(todaydate+datetime.timedelta(days=n)) #date want to address
	future=then+' '+t #datetime format for finding in json
	indexf=json.find(future) # index of datetime
	indexh=json.rfind('"humidity"',0,indexf) #starting index of parameter's required value
	end=json.rfind(',"temp_kf',0,indexf) #end index of parameter's required value
	humidity=json[indexh+11:end]
	return float(humidity)

def get_pressure(json, n=0, t="03:00:00"):
	todaydate=(datetime.date.today()) #store today date as bytes
	then=str(todaydate+datetime.timedelta(days=n)) #date want to address
	future=then+' '+t #datetime format for finding in json
	indexf=json.find(future) # index of datetime
	indexp=json.rfind('"pressure"',0,indexf) #starting index of parameter's required value
	end=json.rfind(',"sea_leve',0,indexf) #end index of parameter's required value
	pressure=json[indexp+11:end]
	return float(pressure)

def get_wind(json, n=0, t="03:00:00"):
	todaydate=(datetime.date.today()) #store today date as bytes
	then=str(todaydate+datetime.timedelta(days=n)) #date want to address
	future=then+' '+t #datetime format for finding in json
	indexf=json.find(future) # index of datetime
	indexw=json.rfind('"speed"',0,indexf) #starting index of parameter's required value
	end=json.rfind(',"deg',0,indexf) #end index of parameter's required value
	windspeed=json[indexw+8:end]
	return float(windspeed)

def get_sealevel(json, n=0, t="03:00:00"):
	todaydate=(datetime.date.today()) #store today date as bytes
	then=str(todaydate+datetime.timedelta(days=n)) #date want to address
	future=then+' '+t #datetime format for finding in json
	indexf=json.find(future) # index of datetime
	indexs=json.rfind('"sea_level"',0,indexf) #starting index of parameter's required value
	end=json.rfind(',"grnd_',0,indexf) #end index of parameter's required value
	sealevel=json[indexs+12:end]
	return float(sealevel)