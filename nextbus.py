import sys
from api import FindNextBus
import re
import logging

if __name__ == "__main__":

    #unittest.main()
    #print(sys.argv)
    if len(sys.argv)<4: #handling edge cases
        logging.warning('You need to provide complete arguments e.g. nextbus.py "METRO Green Line" "Target Field Station Platform 1" "south"')
        exit()
    
    route = sys.argv[1]
    stop = sys.argv[2]
    direction = sys.argv[3]
    try:
        buses = FindNextBus(route,stop,direction)
        departues = buses.get_time_point_departures()       
        
        if len(departues) >0 :
            earlyBus = departues[0]
            minutes = buses.parse_datetime(earlyBus['DepartureTime'])
            print("{} Minutes".format(minutes))
            logging.info("No Bus Available")
        #print(earlyBus['DepartureTime'])        
    except RuntimeError as e:
        logging.info("No Bus Available")
        logging.error(e)

    
    

 




