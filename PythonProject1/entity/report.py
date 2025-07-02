# entity/report.py
from datetime import date

class report:
    def __init__(self,
                 reportID,
                 incidentID,
                 reportingOfficer,
                 reportDate,
                 reportDetails,
                 status):
        self.reportID         = reportID
        self.incidentID       = incidentID
        self.reportingOfficer = reportingOfficer
        self.reportDate       = reportDate
        self.reportDetails    = reportDetails
        self.status           = status

    # getters
    def getReportID(self):         return self.reportID
    def getIncidentID(self):       return self.incidentID
    def getReportingOfficer(self): return self.reportingOfficer
    def getReportDate(self):       return self.reportDate
    def getReportDetails(self):    return self.reportDetails
    def getStatus(self):           return self.status

    # setters
    def set_ReportID(self, reportID):
        if not isinstance(reportID, int):
            raise TypeError("reportID must be an integer")
        self.reportID = reportID

    def set_IncidentID(self, incidentID):
        if not isinstance(incidentID, int):
            raise TypeError("incidentID must be an integer")
        self.incidentID = incidentID

    def set_ReportingOfficer(self, reportingOfficer):
        if not isinstance(reportingOfficer, int):
            raise TypeError("reportingOfficer must be an integer (OfficerID)")
        self.reportingOfficer = reportingOfficer

    def set_ReportDate(self, reportDate):
        if not isinstance(reportDate, date):
            raise TypeError("reportDate must be a date")
        self.reportDate = reportDate

    def set_ReportDetails(self, reportDetails):
        if not isinstance(reportDetails, str):
            raise TypeError("reportDetails must be a string")
        self.reportDetails = reportDetails

    def set_Status(self, status):
        if not isinstance(status, str):
            raise TypeError("status must be a string")
        self.status = status