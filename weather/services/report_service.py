import datetime
from typing import List
from models.location import Location
from models.report import Report

__reports: List[Report] = [] # Keeping everything simple, will be replaced with real database

async def get_reports() -> List[Report]:
    return list(__reports)


async def add_report(description: str, location: Location) -> Report:
    report = Report(location=location, description=description, created=datetime.datetime.now())

    # Will be Replaced with saving to database
    __reports.append(report)
    __reports.sort(key=lambda report: report.created, reverse=True)

    return report