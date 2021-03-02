"""
Created on 01 March 2021

@author: conorkiy@gmail.com
"""


import dbinfo
import traceback
import requests
import datetime
import time
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Float, String, DateTime, insert


"""
API variables
"""
WEATHER = "http://api.openweathermap.org/data/2.5/weather?"
CITY = "Dublin,IE"


"""
Create engine - connect to database
"""
engine = create_engine("mysql+mysqlconnector://{}:{}@{}:3306/{}".format(dbinfo.USER, dbinfo.PASS, dbinfo.URI, dbinfo.DBNAME))

meta = MetaData()

weather = Table(
    'weather', meta,
    Column('main', String(256)),
    Column('description', String(256)),
    Column('temp', Integer),
    Column('rainfall', Float),
    Column('windspeed', Integer),
    Column('time', DateTime)
)


"""
main
"""
def main():
    while True:
        try:

            curr_weather = requests.get(WEATHER, params={"q": CITY, "appid": dbinfo.OW_APIkey})
            values = get_weather(curr_weather.json() )
            insert = weather.insert().values(values)
            engine.execute(insert)

            time.sleep(60*60)

        except:

            print(traceback.format_exc())
    
    return