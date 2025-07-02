from datetime import date
class Incident:
    def __init__(self,incidentID=None,incidentType=None,incidentDate:date=None ,Location=None,Description=None ,Status=None,VictimID=None, SuspectId=None):
        self.incidentID = incidentID
        self.incidentType = incidentType
        self.incidentDate = incidentDate
        self.Location = Location
        self.Description = Description
        self.Status = Status
        self.VictimID = VictimID
        self.SuspectId = SuspectId
    def getIncidentID(self):
        return self.incidentID
    def getIncidentType(self):
        return self.incidentType
    def getIncidentDate(self):
        return self.incidentDate
    def getLocation(self):
        return self.Location
    def getDescription(self):
        return self.Description
    def getStatus(self):
        return self.Status
    def getVictimID(self):
        return self.VictimID
    def getSuspectId(self):
        return self.SuspectId

    def set_IncidentID(self,incidentID):
        if not isinstance(incidentID,int):
            raise TypeError("incident must be an integer")
        else:
            self.incidentID = incidentID
    def set_incidentType(self,incidentType):
        if not isinstance(incidentType,str):
            raise TypeError("incident must be an string")
        else:
            self.incidentType = incidentType
    def set_incidentDate(self,incidentDate):
        if not isinstance(incidentDate,date):
            raise TypeError("incident must be an date")
        else:
            self.incidentDate = incidentDate
    def set_Location(self,Location):
        self.Location = Location
    def set_Description(self,Description):
        if not isinstance(Description,str):
            raise TypeError("incident must be an string")
        else:
            self.Description = Description
    def set_Status(self,Status):
        if not isinstance(Status,str):
            raise TypeError("incident must be an string")
        else:
            self.Status = Status
    def set_VictimID(self,VictimID):
        if not isinstance(VictimID,int):
            raise TypeError("incident must be an integer")
        else:
            self.VictimID = VictimID
    def set_SuspectId(self,SuspectId):
        if not isinstance(SuspectId,int):
            raise TypeError("incident must be an integer")
        else:
            self.SuspectId = SuspectId



