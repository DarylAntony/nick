#main.py
import requests
from random import randint
import time
from BeautifulSoup import BeautifulSoup

#PyMongo dependencies
import sys, os
import datetime
import pymongo
from pymongo import MongoClient

USER_AGENT_STRING = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'

from credentials import *

# import ipdb; ipdb.set_trace()

print test()