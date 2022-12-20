import fastapi
from typing import List
from services.report_service import get_reports, add_report, search_report
from models.report import Report
 
router = fastapi.APIRouter()

@router.get('/api/reports', name='all_reports')
async def reports_get(limit: int = 10, skip: int = 0) -> List[Report]:
    reports = get_reports(limit, skip)
    
    return fastapi.responses.JSONResponse(reports)


@router.post('/api/reports', name='add_report', status_code=201, response_model=Report)
async def reports_post(report: Report) -> Report:
    return add_report(report.description, report.location)


@router.get('/api/search', name='search_report')
async def search_report_get(query: str, find_one: bool = True):
    if find_one:
        result = search_report(query, find_one)
    else:
        result = search_report(query, find_one)

    if result == 404:
        return fastapi.responses.JSONResponse({'details' : 'Not Found !'}, 404)
    
    return result