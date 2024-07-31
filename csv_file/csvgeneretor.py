
import csv
#import logging


def csv_generator(file_name:str,header:[],content:[]):
    try:
        with open(file_name, 'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for j in content:
                #print(j)
                writer.writerow(j)
    except Exception as e:
        print("Error message !!!! ",e)
        #logging.info(e)





