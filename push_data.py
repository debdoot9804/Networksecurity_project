from dotenv import load_dotenv
from collections.abc import MutableMapping



import os
import sys
import json


load_dotenv()
MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def csv_to_json(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_mongo(self,records,database,collection):
        try:
            self.records=records
            self.database=database
            self.collection=collection
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL) 
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)

            return(len(self.records))
        except:
            raise NetworkSecurityException(e,sys)
           
if __name__=='__main__':
    FILE_PATH ="network_data\phisingData.csv"
    DATABASE="DEBDOOT"
    Collection="Network Data"
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json(FILE_PATH) 
    print(records)
    no_of_records=networkobj.insert_mongo(records,DATABASE,Collection)
    print(no_of_records)