class IncidentNumberNotFoundException(Exception):
    def __init__(self,message="the incidentID is not exist"):
        self.message = message
        super().__init__(self.message)
class VictimNumberNotFoundException(Exception):
    def __init__(self,message="the victimID is not exist"):
        self.message = message
        super().__init__(self.message)
class SuspectNumberNotFoundException(Exception):
    def __init__(self,message="the suspectID is not exist"):
        self.message=message
        super().__init__(self.message)
class CaseNumberNotFoundException(Exception):
    def __init__(self,message="the caseID is not exist"):
        self.message=message
        super().__init__(self.message)
