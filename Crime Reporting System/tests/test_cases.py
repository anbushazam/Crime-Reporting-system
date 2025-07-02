from http import server

import pytest
from dao.iCrimeAnalysisServiceImpl import CrimeAnalysisServiceImpl
from entity.incident import Incident
from myexceptions import VictimNumberNotFoundException
from myexceptions import SuspectNumberNotFoundException
from myexceptions import CaseNumberNotFoundException
from myexceptions import IncidentNumberNotFoundException
from datetime import date
from entity.Victim import Victim
from entity.Suspect import Suspect
from entity.Cases import case
test_impl=CrimeAnalysisServiceImpl()
def test_creation_incidents():
    incidentType = "Theft"
    incidentDate = date.today()
    location = "67.88,-45.65"
    Description = "just for testing"
    status = "Resolved"
    VictimID = 1002
    SuspectID = 1002
    new_incident = Incident(
            incidentType=incidentType,
            incidentDate=incidentDate,
            Location=location,
            Description=Description,
            Status=status,
            VictimID=VictimID,
            SuspectId=SuspectID
        )

    t = test_impl.create_incident(new_incident)
    assert t is True
    cursor=test_impl._connection.cursor()
    cursor.execute("SELECT * FROM incidents order by incidentID desc limit 1")
    acc=cursor.fetchone()
    assert acc is not None
    assert acc[1]==new_incident.incidentType
    assert acc[2].date()==new_incident.incidentDate
    assert acc[3]==new_incident.Location
    assert acc[4]==new_incident.Description
    assert acc[5]==new_incident.Status
    assert acc[6]==new_incident.VictimID
    assert acc[7]==new_incident.SuspectId




def test_update_status_invalid():
    invalid_id=8088
    status_sample="Closed"
    with pytest.raises(IncidentNumberNotFoundException) as e:
        test_impl.update_incident_status(invalid_id, status_sample)
    assert "not found" in str(e.value)

def test_update_status_sucess():
    valid_id=20
    status_sample="Closed"
    cursor=test_impl._connection.cursor()
    cursor.execute("UPDATE incidents SET status=%s WHERE incidentID=%s",(status_sample,valid_id))
    test_impl._connection.commit()
    cursor.execute("SELECT status FROM incidents WHERE incidentID=%s",(valid_id,))
    updated_status=cursor.fetchall()
    cursor.close()
    assert "Closed" in updated_status[0]

def test_create_victim():
    v = Victim(None, "John", "Doe", date(1990, 5, 10), "Male", "123 Street", "1234567890")
    assert test_impl.create_victim(v) == True

def test_get_victim_details_valid():
    victim_id = 1001
    result = test_impl.get_victimID_database(victim_id)
    assert result is not None
    assert result[0][0]==victim_id



def test_get_victims_by_gender():
    result = test_impl.get_victims_by_gender("Male")
    assert isinstance(result, list)

def test_get_victims_by_dob():
    dob = date(1990, 5, 10)
    result = test_impl.get_victims_by_dob(dob)
    assert isinstance(result, list)

def test_create_case():
    case_details = "Stolen wallet investigation"
    incident_id = 2  # Make sure this exists
    assert test_impl.create_newCase(case_details, incident_id) == True

def test_get_case_details_valid():
    case_id = 1
    result = test_impl.get_CaseDetails(case_id)
    assert result[0][0] == case_id

def test_get_case_details_invalid():
    with pytest.raises(Exception):
        test_impl.get_CaseDetails(999)

def test_update_case_details():
    case_id = 1
    incident_id = 2
    new_details = "Updated case notes"
    assert test_impl.update_CaseDteails(case_id, new_details,incident_id) == True

def test_list_all_cases():
    result = test_impl.get_All_Cases()
    assert isinstance(result, list)


