import fastapi
from typing import List
from services.report_service import get_reports, add_report
from models.report import Report
 
router = fastapi.APIRouter()

@router.get('/api/reports', name='all_reports')
async def reports_get(limit: int = 10, skip: int = 0) -> List[Report]:
    reports = get_reports(limit, skip)
    
    return fastapi.responses.JSONResponse(reports)


@router.post('/api/reports', name='add_report', status_code=201, response_model=Report)
async def reports_post(report: Report) -> Report:
    return add_report(report.description, report.location)