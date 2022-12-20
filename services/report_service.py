import datetime
from typing import List
from models.location import Location
from models.report import Report
from database.db import ReportDB

__db = ReportDB()

def report_helper(report):
    return {
        '_id' : str(report['_id']),
        'description' : report['description'],
        'location' : report['location'],
        'created' : report['created'].strftime('%I:%M:%S%p %d%b%Y'),
    }


def get_reports(limit: int = None, skip: int = 0) -> List[Report]:
    if limit:
        reports = __db.get_reports(limit, skip)
    else:
        reports = __db.get_reports(skip=skip)

    reports = [report_helper(report) for report in reports]

    reports_count = __db.counter()
    data = {'count' : reports_count, 'reports' : reports}
    
    return data


def search_report(query: str, find_one: bool = True):
    if find_one:
        result = __db.search(query)
        if result:
            result = report_helper(result)
        else:
            result = 404
    else:
        reports = __db.search(query, find_one=False)
        result = [report_helper(report) for report in reports]
        if len(result) == 0:
            result = 404
            
    return result


def add_report(description: str, location: Location) -> Report:
    report = Report(location=location, description=description, created=datetime.datetime.now())

    __db.add_report(report)
    
    return report