from datetime import datetime, timedelta
from time import time
import unittest
import requests
import yaml
import re
config = yaml.safe_load(open("./config.yaml"))
import logging
#“Express - Target - Hwy 252 and 73rd Av P&R - Mpls” “Target North Campus Building F” “south”


BASEURL = config["baseurl"]

class FindNextBus:

    def __init__(self,route,stop,direction):
        self.route = route
        self.stop = stop
        self.direction = direction
        self.route_id = self.get_route_id()
        self.direction_id = self.get_direction_id()
        self.stop_id = self.get_stop_id()

    
    def get_route_id(self):
        #print(BASEURL.format('Routes'))
        data = requests.get(BASEURL.format('Routes')).json()        
        route_id_ = None
        for item in data:
            #text.lower() != text.upper().lower()
            if self.route.casefold() == item['Description'].casefold():
                return item["Route"]
        raise RuntimeError("{} is not a valid route.".format(self.route))
        

    def get_direction_id(self):
        
        #print('---------------------------------Directions--------------------------------------------------------')
        #print('GetDirections operation - http://svc.metrotransit.org/NexTrip/Directions/{ROUTE}')
        #print(BASEURL.format("Directions/{}".format(self.route_id)))        
        resp = requests.get(BASEURL.format("Directions/{}".format(self.route_id)))
        directions = resp.json()
        #print(directions)
        for direction in directions:
            if self.direction.casefold() in direction["Text"].casefold():
                return direction["Value"]
        raise RuntimeError("{} is not a valid direction.".format(self.direction))

    def get_stop_id(self):        
        #print('-------------------------------Stops----------------------------------------------------------')
        #print('GetStops operation - http://svc.metrotransit.org/NexTrip/Stops/{ROUTE}/{DIRECTION}')
        #print(BASEURL.format("Stops/{0}/{1}".format(self.route_id,self.direction_id)))
        resp = requests.get(BASEURL.format("Stops/{0}/{1}".format(self.route_id,self.direction_id)))
        stops = resp.json()
        #print(stops)
        for stop in stops:
            if self.stop.casefold() in stop["Text"].casefold():
                return stop["Value"]
        raise RuntimeError("{} is not a valid direction.".format(self.direction))

    def get_departure(self):
        #print('-------------------------------GetDepartures----------------------------------------------------------')
        #print('GetDepartures operation - http://svc.metrotransit.org/NexTrip/{STOPID}')
        #print(BASEURL.format(self.stop_id))
        resp = requests.get(BASEURL.format(self.stop_id))
        data = resp.json()
        return data

    def get_time_point_departures(self):
        #print('-------------------------------GetTimepointDepartures ----------------------------------------------------------')
        #print('GetDepartures operation -  http://svc.metrotransit.org/NexTrip/{ROUTE}/{DIRECTION}/{STOP}')
        #print(BASEURL.format("{self.route_id}/{self.direction_id}/{self.stop_id}".format(self=self)))
        resp = requests.get(BASEURL.format("{self.route_id}/{self.direction_id}/{self.stop_id}".format(self=self)))
        data = resp.json()
        return data


    def parse_datetime(self,departure_time):        
        s = departure_time
        pattern = '(\d+)([+,-])(\d+)'
        p = re.compile(pattern)
        try:
            capture =  p.findall(s)[0]#first element of tuple
            timestamp = int(capture[0])

            hour = 0
            try:
                hour = int(capture[1]+capture[2])
            except:
                print('Only timestamp present')

            bus_time = datetime.fromtimestamp(timestamp / 1000)
            current_time = datetime.now()
            minutes = str(bus_time - current_time).split(":")[1] # get the minutes from the timestamps
            return int(minutes)
        except:
            pattern = '(\d+)'
            p = re.compile(pattern)
            capture =  p.findall(s)[0]
            timestamp = int(capture[0])
            bus_time = datetime.fromtimestamp(timestamp / 1000)
            current_time = datetime.now()
            minutes = str(bus_time - current_time).split(":")[1] # get the minutes from the timestamps
            return int(minutes)
            print('No capture Group')
        #print(type(capture))#This is tuple
        


