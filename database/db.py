import pymongo
import os
from typing import List
from models.report import Report

class ReportDB:
    '''
        Manage database actions.
    '''

    def __init__(self):
        self.client = pymongo.MongoClient(
            host=os.getenv('HOST_DB'), port=int(os.getenv('PORT_DB')),
            username=os.getenv('USER_DB'), password=os.getenv('PASSWORD_DB')
        )
        self.database = self.client['weather_api']
        self.collection = self.database['reports']
    
    def add_report(self, report: Report) -> str:
        '''Add new report to database'''
        data = {
            'description' : report.description,
            'location' : {
                'city' : report.location.city,
                'state' : report.location.state,
                'country' : report.location.country,
            },
            'created' : report.created
        }
        
        result = self.collection.insert_one(data)
        
        return f'Result : {result.inserted_id}'

    def get_reports(self, limit: int = None) -> List[Report]:
        '''Return a list of reports'''
        if limit:
            results = list(self.collection.find({}).limit(limit))
        else:
            results = list(self.collection.find({}))

        return results
    
    def counter(self) -> int:
        result = self.collection.count_documents({})

        return result