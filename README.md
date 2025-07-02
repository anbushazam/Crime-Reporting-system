#🚔 Crime Analysis and Reporting System (CARS)
A menu-driven Python application to manage and analyze crime-related data including incidents, victims, suspects, and case records. This project is built using MySQL for database handling and Rich for visually appealing console outputs. It features custom exceptions, structured DAO architecture, and complete CRUD support.

🗂️ Project Structure
CrimeAnalysisSystem/
│
├── dao/
│   ├── icarService.py
│   ├── iCrimeAnalysisServiceImpl.py
│
├── entity/
│   ├── incident.py
│   ├── Victim.py
│   ├── Suspect.py
│   ├── Case.py
│
├── util/
│   ├── database_connection.py
│   ├── db.properties
│
├── exception/
│   ├── myexceptions.py
│
├── main/
│   ├── main.py
│
├── tests/
│   ├── test_cases.py
│
└── README.md


📌 Features
✅ Incident Management
o Create and record new incidents

o Update incident statuses (e.g., Open, Closed)

o Search incidents by type

o Filter incidents by date range

o Generate incident-specific reports

o View full details of any incident

✅ Victim Management
o View victim details by ID

o List victims filtered by gender

o List victims by date of birth

o Automatically create victim records if new

✅ Suspect Management
o View suspect details by ID

o List suspects filtered by gender

o List suspects by date of birth

o Automatically create suspect records if new

✅ Case Management
o Create a new case linked to an incident

o View and update case details

o List all existing cases

# Tools and packages used

| Tool/Library               | Purpose                             |
| -------------------------- | ----------------------------------- |
| **Python 3.13+**           | Core programming language           |
| **MySQL**                  | Relational database management      |
| **mysql-connector-python** | Python-MySQL DB integration         |
| **Rich**                   | Console table and layout formatting |
| **PyTest**                 | Unit testing                        |


🧪 Testing
o Unit tests are written using PyTest covering:

o Incident creation and status update

o Victim and suspect details validation

o Custom exception handling

o Case creation and updates

# Run tests using:

```bash
pytest tests/test_cases.py

💡 Notes
o Ensure MySQL server is running and db.properties has correct credentials.

o Incident ID is auto-incremented; Victim/Suspect IDs can be created interactively if missing.

o Tables are printed using Rich for better visual clarity.

o Modular, object-oriented structure using interface and DAO layers.

# 📸 Sample Output
+-----------+------------+------------+--------------+--------------------------+--------------+-----------+------------+
| Incident  | Type       | Date       | Location     | Description              | Status       | Victim ID | Suspect ID |
+-----------+------------+------------+--------------+--------------------------+--------------+-----------+------------+
| 12        | Burglary   | 2025-07-01 | 13.0732,80.25| Forced entry detected    | Under Invest.| 1011      | 1011       |
+-----------+------------+------------+--------------+--------------------------+--------------+-----------+------------+


