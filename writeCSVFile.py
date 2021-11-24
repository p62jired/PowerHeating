# Pre-requisite - Import the writer class from the csv module
from csv import writer
import time
import json
jsonFilePath = "/var/lib/docker/volumes/iot-stack-tutorial_noderedData/_data/bind.json"

tLoggerStart = time.perf_counter()
#Load JSON struct from JSON file into global variable
while True:
    tLoggerCurrent = time.perf_counter()
    if tLoggerCurrent-tLoggerStart > 5:
        tLoggerStart = time.perf_counter()
        tLoggerCurrent = time.perf_counter()
        time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) 

        
        # Pre-requisite - The CSV file should be manually closed before running this code.

        # First, open the old CSV file in append mode, hence mentioned as 'a'
        # Then, for the CSV file, create a file object
        with open(jsonFilePath) as jsonFile:
            jsonSystem = json.load(jsonFile)
            jsonFile.close()
        isHeatingActivated =    jsonSystem["ISR"][1]["ContactorOn"][0] \
                or jsonSystem["ISR"][1]["ContactorOn"][0] \
                or jsonSystem["ISR"][1]["ContactorOn"][0]

        # The data assigned to the list 
        list_data=[time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),jsonSystem["Lufttemperatur"]\
                  ,jsonSystem["Windgeschwindigkeit"],jsonSystem["Niederschlagsmenge"]\
                  ,jsonSystem["Niederschlagsart"],jsonSystem["UV-Index"]]

        if   isHeatingActivated:      
            with open('logs/logger.csv', 'a', newline='') as f_object:  
                # Pass the CSV  file object to the writer() function
                writer_object = writer(f_object)
                # Result - a writer object
                # Pass the data in the list as an argument into the writerow() function
                writer_object.writerow(list_data)  
                # Close the file object
                f_object.close()