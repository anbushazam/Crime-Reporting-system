from datetime import date
from abc import ABC, abstractmethod
from entity.Cases import case
import incident
from entity.incident import Incident
from entity.report import report
from entity.Victim import Victim
from entity.Suspect import Suspect
class ICrimeAnalysisService(ABC):

    @abstractmethod
    def create_incident(self, incident: Incident) -> bool:
        pass
    @abstractmethod
    def create_victim(self, Victim: Victim) -> bool:
        pass
    @abstractmethod
    def create_suspect(self, Suspect:Suspect) -> bool:
        pass
    @abstractmethod
    def update_incident_status(self, incident_id: int, status: str) -> bool:
        pass

    @abstractmethod
    def get_incidents_in_date_range(self, start_date: date, end_date: date) -> list[Incident]:
        pass

    @abstractmethod
    def search_incidents(self, incident_type: str) -> list[Incident]:
        pass

    @abstractmethod
    def generate_incident_report(self, incident: Incident) :
        pass
    @abstractmethod
    def create_newCase_with_newIncidents(self,caseDescription,inc:incident):
        pass
    @abstractmethod
    def create_newCase(self,caseDescription,incidentID):
        pass
    @abstractmethod
    def get_CaseDetails(self, caseID:int):
        pass
    @abstractmethod
    def update_CaseDteails(self,case_id,caseDescription,incidentID):
        pass
    @abstractmethod
    def get_All_Cases(self):
        pass
    # the below functions are used in previous methdos for flexibility
    @abstractmethod
    def get_incidentID_database(self,incidentID:int):
        pass
    @abstractmethod
    def get_victimID_database(self,victimID:int):
        pass
    @abstractmethod
    def get_SuspectID_database(self,SuspectID:int):
        pass
    @abstractmethod
    def get_victim_details(self, victim_id: int) -> tuple:
        pass

    @abstractmethod
    def get_victims_by_gender(self, gender: str) -> list:
        pass

    @abstractmethod
    def get_victims_by_dob(self, dob: str) -> list:
        pass

    @abstractmethod
    def get_suspect_details(self, suspect_id: int) -> tuple:
        pass

    @abstractmethod
    def get_suspects_by_gender(self, gender: str) -> list:
        pass

    @abstractmethod
    def get_suspects_by_dob(self, dob: str) -> list:
        pass
    @abstractmethod
    def get_incident_details(self, incident_id: int):
        pass