import datetime
from typing import List
from models.location import Location
from models.report import Report
from database.db import ReportDB

__db = ReportDB()

def get_reports(limit: int = None, skip: int = 0) -> List[Report]:
    def report_helper(report):
        return {
            '_id' : str(report['_id']),
            'description' : report['description'],
            'location' : report['location'],
            'created' : report['created'].strftime('%I:%M:%S%p %d%b%Y'),
        }

    if limit:
        reports = __db.get_reports(limit, skip)
    else:
        reports = __db.get_reports(skip=skip)

    reports = [report_helper(report) for report in reports]

    reports_count = __db.counter()
    data = {'count' : reports_count, 'reports' : reports}
    
    return data


def add_report(description: str, location: Location) -> Report:
    report = Report(location=location, description=description, created=datetime.datetime.now())

    __db.add_report(report)
    
    return report