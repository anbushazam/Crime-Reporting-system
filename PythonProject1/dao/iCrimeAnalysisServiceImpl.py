import incident
from dao.icarService import ICrimeAnalysisService
from util.database_connection import DB_connection
from datetime import date
from entity.incident import Incident
from entity.Cases import case
from entity.report import report
from entity.Victim import Victim
from entity.Suspect import Suspect
from myexceptions import VictimNumberNotFoundException
from myexceptions import SuspectNumberNotFoundException
from myexceptions import CaseNumberNotFoundException
from myexceptions import IncidentNumberNotFoundException
class CrimeAnalysisServiceImpl(ICrimeAnalysisService):
    _connection=None
    def __init__(self):
        if CrimeAnalysisServiceImpl._connection is None:
            CrimeAnalysisServiceImpl._connection=DB_connection.get_connection()
    def create_incident(self,incident:Incident):
        cursor=self._connection.cursor()
        if incident.incidentID is None:
            query="""insert into incidents(incidentType, incidentDate, location,
            description, status, VictimID, SuspectID) values (%s,%s,%s,%s,%s,%s,%s)"""
            value = ( incident.incidentType, incident.incidentDate, incident.Location,
                     incident.Description, incident.Status, incident.VictimID, incident.SuspectId)
            cursor.execute(query, value)
        else:
            query1="""insert into incidents(incidentID, incidentType, incidentDate, location,
            description, status, VictimID, SuspectID) values (%s,%s,%s,%s,%s,%s,%s,%s)"""
            value1=(incident.incidentID,incident.incidentType, incident.incidentDate, incident.Location,incident.Description, incident.Status, incident.VictimID, incident.SuspectId)
            cursor.execute(query1,value1)
        self._connection.commit()
        return True

    def create_victim(self, victim: Victim) -> int:
        cursor = self._connection.cursor()

        if victim.victim_id is None:
            query = """insert into victims (First_name, Last_name,DateOfBirth , Gender, Contact_address, Contact_phone_number) values (%s, %s, %s, %s, %s, %s) """
            values = (
                victim.first_name,
                victim.last_name,
                victim.date_of_birth,
                victim.gender,
                victim.address,
                victim.phone_number
            )
            cursor.execute(query, values)
        else:
            query = """
                    insert into victims (VictimID, First_name, Last_name,DateOfBirth , Gender, Contact_address, Contact_phone_number) values (%s, %s, %s, %s, %s, %s, %s)  """
            values = (
                victim.victim_id,
                victim.first_name,
                victim.last_name,
                victim.date_of_birth,
                victim.gender,
                victim.address,
                victim.phone_number
            )
            cursor.execute(query, values)

        self._connection.commit()
        return True

    def create_suspect(self, suspect: Suspect) -> int:
        cursor = self._connection.cursor()

        if suspect.suspect_id is None:
            query = """
                    insert into suspects (First_name, Last_name,DateOfBirth , Gender, Contact_address, Contact_phone_number) VALUES (%s, %s, %s, %s, %s, %s) """
            values = (
                suspect.first_name,
                suspect.last_name,
                suspect.date_of_birth,
                suspect.gender,
                suspect.address,
                suspect.phone_number
            )
            cursor.execute(query, values)
        else:
            query = """
                    insert into suspects (SuspectID, First_name, Last_name,DateOfBirth , Gender, Contact_address, Contact_phone_number) values(%s, %s, %s, %s, %s, %s, %s) """
            values = (
                suspect.suspect_id,
                suspect.first_name,
                suspect.last_name,
                suspect.date_of_birth,
                suspect.gender,
                suspect.address,
                suspect.phone_number
            )
            cursor.execute(query, values)

        self._connection.commit()
        return cursor.lastrowid if suspect.suspect_id is None else suspect.suspect_id

    def update_incident_status(self, incidentID, Status):
        cursor=self._connection.cursor()
        cursor.execute("""select*from incidents where incidentID=%s""",(incidentID,))
        result=cursor.fetchone()
        if not result:
            raise IncidentNumberNotFoundException(f"incidentID={incidentID} not found")
        query1="""update incidents set status=%s where incidents.incidentID=%s"""
        value=(Status, incidentID)
        cursor.execute(query1,value)
        self._connection.commit()

        return True

    def search_incidents(self,incidentType:str):
        cursor=self._connection.cursor()
        query="""select * from incidents where incidents.incidentType=%s"""""
        value=(incidentType,)
        cursor.execute(query,value)
        results=cursor.fetchall()
        return results
    def get_incidents_in_date_range(self, startDate: date, endDate: date):
        cursor = self._connection.cursor()
        query = "SELECT * FROM incidents WHERE incidentDate >= %s AND incidentDate <= %s"
        values = (startDate, endDate)
        cursor.execute(query, values)
        return cursor.fetchall()

    def generate_incident_report(self,incidentID):
        cursor=self._connection.cursor()
        query="""select * from reports as r join incidents as i on i.incidentID=r.incidentID where i.incidentID=%s"""
        value=(incidentID,)
        cursor.execute(query,value)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        result = [dict(zip(columns, row)) for row in rows]

        return result
    def create_newCase_with_newIncidents(self,caseDescription,incident:Incident):
        cursor=self._connection.cursor()
        query="""insert into cases(caseDescription,incidentID) values (%s,%s)"""
        values=(caseDescription,incident.incidentID)
        cursor.execute(query,values)
        self._connection.commit()
        return True
    def create_newCase(self,caseDescription,incidentID):
        cursor=self._connection.cursor()
        query="""insert into cases(caseDescription,incidentID) values (%s,%s)"""
        values=(caseDescription,incidentID)
        cursor.execute(query,values)
        self._connection.commit()
        return True
    def get_CaseDetails(self,caseID:int):
        cursor=self._connection.cursor()
        query0 = """select case_id from cases where case_id = %s"""
        values = (caseID,)
        cursor.execute(query0, values)
        che=cursor.fetchone()
        if che is None:
            raise CaseNumberNotFoundException(f"case_id {caseID} not found")
        query="""select * from cases where case_id=%s"""
        value=(caseID,)
        cursor.execute(query,value)
        return cursor.fetchall()
    def update_CaseDteails(self,case_id,caseDescription,incidentID):
        cursor=self._connection.cursor()
        query="""update cases set caseDescription=%s where case_id=%s"""
        value=(caseDescription,case_id)
        cursor.execute(query,value)
        self._connection.commit()
        query1="""update cases set incidentID=%s where case_id=%s"""
        value=(incidentID,case_id)
        cursor.execute(query1,value)
        self._connection.commit()
        return True

    def get_All_Cases(self):
        cursor=self._connection.cursor()
        query="""select * from cases"""
        cursor.execute(query)
        return cursor.fetchall()

    def get_incidentID_database(self, incidentID: int):
        cursor=self._connection.cursor()
        query="""select incidentID from incidents where incidentID=%s """
        values= (incidentID,)
        cursor.execute(query,values)
        return cursor.fetchall()
    def get_victimID_database(self,victimID:int):
        cursor=self._connection.cursor()
        query="""select VictimID from victims where VictimID=%s"""
        values= (victimID,)
        cursor.execute(query,values)
        return cursor.fetchall()

    def get_SuspectID_database(self,SuspectID:int):
        cursor = self._connection.cursor()
        query = """select SuspectID from suspects where SuspectID=%s"""
        values= (SuspectID,)
        cursor.execute(query,values)
        return cursor.fetchall()

    def get_victim_details(self, victim_id: int):
        cursor = self._connection.cursor()
        query0="""select VictimID from victims where VictimID=%s"""
        values= (victim_id,)
        cursor.execute(query0,values)
        che=cursor.fetchone()
        if che is None:
            raise VictimNumberNotFoundException(f"Victim ID {victim_id} not found")
        else:
            cursor.execute("SELECT * FROM victims WHERE VictimID= %s", (victim_id,))
            return cursor.fetchone()

    def get_victims_by_gender(self, gender: str):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM victims WHERE gender = %s", (gender,))
        return cursor.fetchall()

    def get_victims_by_dob(self, dob: str):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM victims WHERE DateOfBirth = %s", (dob,))
        return cursor.fetchall()

    def get_suspect_details(self, suspect_id: int):
        cursor = self._connection.cursor()
        query0 = """select SuspectID from suspects where SuspectID=%s"""
        values= (suspect_id,)
        cursor.execute(query0,values)
        che=cursor.fetchone()
        if che is None:
            raise SuspectNumberNotFoundException(f"Suspect ID ID {suspect_id} not found")
        else:
            cursor.execute("SELECT * FROM suspects WHERE SuspectID = %s", (suspect_id,))
            return cursor.fetchone()

    def get_suspects_by_gender(self, gender: str):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM suspects WHERE Gender = %s", (gender,))
        return cursor.fetchall()

    def get_suspects_by_dob(self, dob: str):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM suspects WHERE DateOfBirth = %s", (dob,))
        return cursor.fetchall()

    def get_incident_details(self, incident_id: int):
        cursor=self._connection.cursor()
        query="""select * from incidents where incidentID=%s """
        values= (incident_id,)
        cursor.execute(query,values)
        return cursor.fetchall()



