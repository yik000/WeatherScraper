"""
Created on 01 March 2021

@author: conorkiy@gmail.com
"""


import dbinfo
import traceback
import requests
import datetime
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Float, String, DateTime, insert


"""
API variables
"""
WEATHER = "http://api.openweathermap.org/data/2.5/weather?"
CITY = "Dublin,IE"

