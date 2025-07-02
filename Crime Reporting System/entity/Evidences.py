# entity/evidence.py
class evidence:
    def __init__(self,
                 evidenceID,
                 description,
                 locationFound,
                 incidentID):
        self.evidenceID   = evidenceID
        self.description  = description
        self.locationFound= locationFound
        self.incidentID   = incidentID

    # getters
    def getEvidenceID(self):    return self.evidenceID
    def getDescription(self):   return self.description
    def getLocationFound(self): return self.locationFound
    def getIncidentID(self):    return self.incidentID

    # setters
    def set_EvidenceID(self, evidenceID):
        if not isinstance(evidenceID, int):
            raise TypeError("evidenceID must be an integer")
        self.evidenceID = evidenceID

    def set_Description(self, description):
        if not isinstance(description, str):
            raise TypeError("description must be a string")
        self.description = description

    def set_LocationFound(self, locationFound):
        if not isinstance(locationFound, str):
            raise TypeError("locationFound must be a string")
        self.locationFound = locationFound

    def set_IncidentID(self, incidentID):
        if not isinstance(incidentID, int):
            raise TypeError("incidentID must be an integer")
        self.incidentID = incidentID