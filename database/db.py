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

    def get_reports(self, limit: int = None, skip: int = 0) -> List[Report]:
        '''Return a list of reports'''
        if limit:
            results = list(self.collection.find({}).skip(skip).limit(limit).sort('_id', -1))
        else:
            results = list(self.collection.find({}).skip(skip).sort('_id', -1))

        return results
    
    def counter(self) -> int:
        result = self.collection.estimated_document_count({})
        return result