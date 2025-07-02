import datetime
from rich.console import Console
from rich.table import Table
from icarService import ICrimeAnalysisService
from iCrimeAnalysisServiceImpl import CrimeAnalysisServiceImpl
from datetime import datetime
from entity.incident import Incident
from myexceptions import IncidentNumberNotFoundException
from myexceptions import VictimNumberNotFoundException
from myexceptions import SuspectNumberNotFoundException
from myexceptions import CaseNumberNotFoundException

def display_rich_table(records, headers):
    console = Console(width=200, soft_wrap=True)
    table = Table(show_lines=True)

    for header in headers:
        table.add_column(header, style="cyan", no_wrap=True, overflow="fold")

    for record in records:
        row = []
        for item in record:
            if isinstance(item, datetime):
                row.append(item.strftime("%Y-%m-%d %H:%M"))
            else:
                row.append(str(item))
        table.add_row(*row)

    console.print(table)

def main():
    service:ICrimeAnalysisService=CrimeAnalysisServiceImpl()
    while True:
        print("\n----------(CRIME REPORTING SYSTEM-----------\n")
        print("1.On Incidents")
        print("2.On Victims")
        print("3. On suspects")
        print("4.On Cases")
        print("5. Exit")
        print("============================================")
        menu=int(input("\nEnter your choice: "))
        while True:
            if menu==1:
                print("\n ON INCIDENTS\n")
                print("1. Create Incident")
                print("2. Update Incident Status")
                print("3. Search Incidents by Type")
                print("4. Get Incidents in Date Range")
                print("5. Generate Incident Report")
                print("6.get a incident details")
                print("0. Exit")
                menu_num = int(input("\nEnter your choice\n: "))
                print("============================================")
                if menu_num == 1:
                    id = int(input("Incident ID: "))
                    typ = input("Incident Type: ")
                    dt = input("Date (YYYY-MM-DD): ")
                    loc = input("Location: ")
                    desc = input("Description: ")
                    status = input("Status: ")
                    vic = int(input("Victim ID: "))
                    susp = int(input("Suspect ID: "))
                    new_incident = Incident(id, typ, dt, loc, desc, status, vic, susp)
                    service.create_incident(new_incident)
                    print("Incident created")
                if menu_num == 2:
                    try:
                        id = int(input("Incident ID: "))
                        st = input("Incident Status: ")
                        service.update_incident_status(id, st)
                        print("Incident updated")
                    except IncidentNumberNotFoundException as e:
                        print("SORRY", e)
                if menu_num == 3:
                    st = input("Incident Type: ")
                    res = service.search_incidents(st)
                    headers = ["Incident ID", "Type", "Date", "Location", "Description", "Status", "Victim ID", "Suspect ID"]
                    display_rich_table(res, headers)
                if menu_num == 4:
                    st_date = input("start date: ")
                    en_date = input("end date: ")
                    results = service.get_incidents_in_date_range(st_date, en_date)
                    headers = ["Incident ID", "Type", "Date", "Location", "Description", "Status", "Victim ID", "Suspect ID"]
                    display_rich_table(results, headers)
                if menu_num == 5:
                    id = int(input("Incident ID: "))
                    results = service.generate_incident_report(id)
                    print("here is the details:")
                    for row in results:
                        for key, value in row.items():
                            print(f"{key}: {value}")
                if menu_num==6:
                    id= int(input("Incident ID: "))
                    results=service.get_incident_details(id)
                    headers = ["Incident ID", "Type", "Date", "Location", "Description", "Status", "Victim ID", "Suspect ID"]
                    display_rich_table(results, headers)
                if menu_num == 0:
                    break

            if menu==2:
                print("\n ON VICTIMS\n")
                print("1. Get victim details")
                print("2. Get victims list by gender")
                print("3. Get victims list by date of birth")
                print("0. Exit")
                menu_num = int(input("\nEnter your choice\n: "))
                print("============================================")
                if menu_num == 1:
                    try:
                        id = int(input("Victim ID: "))
                        result = service.get_victim_details(id)
                        headers = ["Victim ID", "First Name", "Last Name", "Date of Birth", "Gender", "Address", "Phone Number"]
                        display_rich_table([result], headers)
                    except VictimNumberNotFoundException as e:
                        print("\n----------SORRY------------\n", e)
                if menu_num == 2:
                    gender = input("Enter gender: ")
                    results = service.get_victims_by_gender(gender)
                    headers = ["Victim ID", "First Name", "Last Name", "Date of Birth", "Gender", "Address", "Phone Number"]
                    display_rich_table(results, headers)
                if menu_num == 3:
                    dob = input("Enter DOB (YYYY-MM-DD): ")
                    results = service.get_victims_by_dob(dob)
                    headers = ["Victim ID", "First Name", "Last Name", "Date of Birth", "Gender", "Address", "Phone Number"]
                    display_rich_table(results, headers)
                if menu_num == 0:
                    break

            if menu == 3:
                print("\n ON SUSPECTS\n")
                print("1. Get suspect details")
                print("2. Get suspects list by gender")
                print("3. Get suspects list by date of birth")
                print("0. Exit")
                menu_num = int(input("\nEnter your choice\n: "))
                print("============================================")
                if menu_num == 1:
                    try:
                        id = int(input("Suspect ID: "))
                        result = service.get_suspect_details(id)
                        headers = ["Suspect ID", "First Name", "Last Name", "Date of Birth", "Gender", "Address", "Phone Number"]
                        display_rich_table([result], headers)
                    except SuspectNumberNotFoundException as e:
                        print("\n----------SORRY------------\n", e)
                if menu_num == 2:
                    gender = input("Enter gender: ")
                    results = service.get_suspects_by_gender(gender)
                    headers = ["Suspect ID", "First Name", "Last Name", "Date of Birth", "Gender", "Address", "Phone Number"]
                    display_rich_table(results, headers)
                if menu_num == 3:
                    dob = input("Enter DOB (YYYY-MM-DD): ")
                    results = service.get_suspects_by_dob(dob)
                    headers = ["Suspect ID", "First Name", "Last Name", "Date of Birth", "Gender", "Address", "Phone Number"]
                    display_rich_table(results, headers)
                if menu_num == 0:
                    break

            if menu == 4:
                print("\n ON CASES\n")
                print("1. create a new case")
                print("2. get a case details")
                print("3. update a case details")
                print("4. list all cases ")
                print("0. Exit")
                menu_num = int(input("\nEnter your choice\n: "))
                print("============================================")
                if menu_num == 1:
                    id = int(input("Incident ID: "))
                    typ = input("Incident Type: ")
                    dt = input("Date (YYYY-MM-DD): ")
                    loc = input("Location: ")
                    desc = input("Description: ")
                    status = input("Status: ")
                    vic = int(input("Victim ID: "))
                    susp = int(input("Suspect ID: "))
                    check_id = service.get_incidentID_database(id)
                    cd = input(" Enter the case description")
                    if id is None:
                        new_incident = Incident(id, typ, dt, loc, desc, status, vic, susp)
                        service.create_incident(new_incident)
                        service.create_newCase(cd, new_incident)
                        print("new case created")
                    else:
                        service.create_newCase(cd, id)
                if menu_num == 2:
                    try:
                        c_id = int(input("Enter the case ID: "))
                        results = service.get_CaseDetails(c_id)
                        headers = ["Case ID", "Case Description", "Incident ID"]
                        display_rich_table([results], headers)
                    except CaseNumberNotFoundException as e:
                        print("\n----------SORRY------------\n", e)
                if menu_num == 3:
                    c_id = int(input("Enter the case ID: "))
                    new_d = input("Enter the new description to update:")
                    in_id = int(input("Enter the  new incident ID to update: "))
                    service.update_CaseDteails(c_id, new_d, in_id)
                    print("updated case details")
                if menu_num == 4:
                    results = service.get_All_Cases()
                    headers = ["Case ID", "Case Description", "Incident ID"]
                    display_rich_table(results, headers)
                if menu_num == 0:
                    break

        if menu==5:
            break

if __name__ == '__main__':
    main()
