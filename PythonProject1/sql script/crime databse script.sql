create database if not exists crime_database;
use crime_database
-- TABLE CREATIONS

create table if not exists Victims(
VictimID int auto_increment primary key,
First_name char(100),
Last_name char(100),
DateOfBirth date,
Gender char(50),
Contact_address varchar(200),
Contact_phone_number int
)auto_increment =1000;



create table if not exists Suspects(
SuspectID int auto_increment primary key,
First_name char(100),
Last_name char(100),
DateOfBirth date,
Gender char(50),
Contact_address varchar(200),
Contact_phone_number int
)auto_increment =1000;



create table if not exists incidents(
incidentID int auto_increment primary key,
incidentType varchar(100),
incidentDate datetime,
location varchar(100),
Description text,
status char(100),
VictimID int,
foreign key (VictimID) references Victims(VictimID) on delete cascade on update cascade,
SuspectID int,
foreign key (SuspectID) references Suspects(SuspectID) on delete cascade on update cascade
)

create table if not exists Law_Enforcement_Agencies(
AgencyID int auto_increment primary key,
AgencyName varchar(50),
Jurisdiction varchar(100),
Contact_address varchar(200),
Contact_phone_number int
);


create table if not exists Officers(
OfficerID int auto_increment primary key,
First_name char(100),
Last_name char(100),
BadgeNumber varchar(50),
Ranks varchar(50),
Contact_address varchar(200),
Contact_phone_number int,
AgencyID int,
foreign key (AgencyID) references Law_Enforcement_Agencies(AgencyID)
);



create table if not exists Evidence(
EvidenceID int primary key,
Description varchar(200),
Location_Found varchar(200),
incidentID int,
foreign key (incidentID)references incidents(incidentID)
);

create table if not exists Reports(
ReportID int primary key,
incidentID int,
ReportingOfficer int,
ReportDate datetime,
ReportDetails varchar(200),
Status char(50),
foreign key (incidentID) references incidents(incidentID),
foreign key (ReportingOfficer) references Officers(OfficerID)
);

create table cases(
case_id int auto_increment primary key,
caseDescription varchar(500),
incidentID int,
foreign key (incidentID) references incidents(incidentID)
);


-- DATA INSERTION 
insert into Victims (First_name, Last_name, DateOfBirth, Gender, Contact_address, Contact_phone_number) values
('John',    'Smith',    '1980-01-15', 'Male',   '123 Elm St',     5551001),
('Maria',   'Gomez',    '1991-06-10', 'Female', '789 Oak Blvd',   5551002),
('David',   'Lee',      '1985-03-22', 'Male',   '456 Pine Ln',    5551003),
('Sophia',  'Patel',    '1992-12-05', 'Female', '234 Maple Rd',   5551004),
('James',   'Clark',    '1978-07-19', 'Male',   '908 Spruce St',  5551005),
('Emily',   'Chen',     '1989-04-11', 'Female', '712 Cedar Ave',  5551006),
('Daniel',  'Kumar',    '1990-09-08', 'Male',   '300 Hilltop Ct', 5551007),
('Lily',    'Brown',    '1993-11-24', 'Female', '100 Oak Dr',     5551008),
('Robert',  'Jones',    '1982-08-03', 'Male',   '630 Birch Pkwy', 5551009),
('Olivia',  'Mehta',    '1994-01-29', 'Female', '145 River Way',  5551010),
('Kevin',   'Nguyen',   '1983-05-18', 'Male',   '78 Summit Blvd', 5551011),
('Grace',   'Wilson',   '1995-03-14', 'Female', '20 Forest Ln',   5551012),
('Thomas',  'Green',    '1987-10-10', 'Male',   '310 Lake Dr',    5551013),
('Zara',    'Sharma',   '1990-06-21', 'Female', '90 Ocean Rd',    5551014),
('Luke',    'Turner',   '1981-02-26', 'Male',   '670 Field St',   5551015),
('Priya',   'Rao',      '1996-11-13', 'Female', '805 Coral Ave',  5551016),
('Henry',   'Morgan',   '1988-09-12', 'Male',   '481 Palm St',    5551017),
('Asha',    'Malik',    '1986-07-01', 'Female', '91 Ivy Cir',     5551018),
('Noah',    'Taylor',   '1992-03-06', 'Male',   '55 Vine Dr',     5551019),
('Diana',   'Knight',   '1993-08-28', 'Female', '120 Breeze Rd',  5551020);

insert into Suspects (First_name, Last_name, DateOfBirth, Gender, Contact_address, Contact_phone_number) values
('Victor', 'Gray',    '1982-02-01', 'Male',   '11 Cross St',     5552001),
('Nora',   'Hill',    '1990-05-21', 'Female', '87 Breeze Blvd',  5552002),
('Liam',   'Fox',     '1986-04-09', 'Male',   '401 Pine Ct',     5552003),
('Sana',   'Khan',    '1992-08-17', 'Female', '28 Horizon Rd',   5552004),
('Alan',   'Wright',  '1983-11-14', 'Male',   '90 Willow Cir',   5552005),
('Chloe',  'Dunn',    '1994-07-29', 'Female', '36 Bay St',       5552006),
('Jason',  'Frost',   '1981-12-19', 'Male',   '50 Canyon Dr',    5552007),
('Riya',   'Shah',    '1995-03-30', 'Female', '102 Crescent Way',5552008),
('Ethan',  'Bishop',  '1988-06-22', 'Male',   '209 Birch Pkwy',  5552009),
('Tina',   'Gupta',   '1991-09-05', 'Female', '15 Coral Ridge',  5552010),
('Kyle',   'Lopez',   '1980-01-12', 'Male',   '67 Fern Rd',      5552011),
('Amy',    'Singh',   '1993-10-28', 'Female', '300 Water Ln',    5552012),
('Chris',  'Bryant',  '1979-04-16', 'Male',   '445 Palm Blvd',   5552013),
('Zoe',    'Patel',   '1987-02-02', 'Female', '33 Ivy Bend',     5552014),
('Ryan',   'Grant',   '1984-11-08', 'Male',   '10 Summit View',  5552015),
('Meera',  'Roy',     '1992-01-26', 'Female', '17 Sunset Ave',   5552016),
('Shawn',  'Evans',   '1989-07-12', 'Male',   '89 Bayfront Ct',  5552017),
('Tara',   'Yadav',   '1990-05-09', 'Female', '56 Mountain Pass',5552018),
('Omar',   'Knight',  '1985-06-04', 'Male',   '63 Golden Hill',  5552019),
('Leah',   'Fernandez','1994-12-23','Female', '77 Breeze Bend',  5552020);

insert into Law_Enforcement_Agencies (AgencyName, Jurisdiction, Contact_address, Contact_phone_number) values
('Metro PD',        'Metro City',    '101 Central Rd',    5553001),
('North Precinct',  'Northville',    '102 North Ave',     5553002),
('South Division',  'Southvale',     '103 South Blvd',    5553003),
('East Wing',       'Eastville',     '104 East St',       5553004),
('West Command',    'Westburg',      '105 West Pkwy',     5553005),
('Midtown Force',   'Midtown',       '106 Midtown Cir',   5553006),
('Harbor Patrol',   'Harbor City',   '107 Harbor Dr',     5553007),
('Lakeside Dept',   'Lakeside',      '108 Lakeview Ct',   5553008),
('Hilltop Bureau',  'Hilltop',       '109 Hilltop Cres',  5553009),
('Central Heights', 'Centrum',       '110 Central Ave',   5553010),
('Elm Station',     'Elmbrook',      '111 Elm St',        5553011),
('Maple Yard',      'Mapleton',      '112 Maple Rd',      5553012),
('River Police',    'Riverdale',     '113 River Way',     5553013),
('Forest HQ',       'Forestville',   '114 Forest Blvd',   5553014),
('Highland Base',   'Highland',      '115 Highland Cir',  5553015),
('Valley HQ',       'Valleytown',    '116 Valley Way',    5553016),
('Skyline PD',      'Skyline City',  '117 Skyline Ave',   5553017),
('Glen Post',       'Glenshire',     '118 Glen Dr',       5553018),
('Sunset Patrol',   'Sunset Bay',    '119 Sunset Rd',     5553019),
('Aurora Dept',     'Aurora Springs','120 Aurora Ln',     5553020);

insert into Officers (First_name, Last_name, BadgeNumber, Ranks, Contact_address, Contact_phone_number, AgencyID) values
('Aaron',  'Davis',  'MD-1001', 'Sergeant', '1 Alpha St',    5554001, 1),
('Bella',  'Nguyen', 'MD-1002', 'Lieutenant','2 Bravo Rd',   5554002, 2),
('Carl',   'Shaw',   'MD-1003', 'Inspector', '3 Charlie Ln', 5554003, 3),
('Dina',   'Singh',  'MD-1004', 'Captain',   '4 Delta Blvd', 5554004, 4),
('Eli',    'Kim',    'MD-1005', 'Constable', '5 Echo Ave',   5554005, 5),
('Fiona',  'Lopez',  'MD-1006', 'Sergeant',  '6 Fox Dr',     5554006, 6),
('Gavin',  'Morris', 'MD-1007', 'Lieutenant','7 Gulf Cres',  5554007, 7),
('Hanna',  'Clark',  'MD-1008', 'Inspector', '8 Hawk Rd',    5554008, 8),
('Ian',    'Wells',  'MD-1009', 'Captain',   '9 Ice Pkwy',   5554009, 9),
('Jade',   'Bose',   'MD-1010', 'Constable', '10 Jet Ave',   5554010,10),
('Kyle',   'Ali',    'MD-1011', 'Detective','11 Kilo St',    5554011,11),
('Lana',   'Reed',   'MD-1012', 'Sergeant', '12 Lima Blvd',  5554012,12),
('Mark',   'Ortiz',  'MD-1013', 'Lieutenant','13 Mike Dr',   5554013,13),
('Nina',   'Chen',   'MD-1014', 'Detective','14 November Ln',5554014,14),
('Oscar',  'Frost',  'MD-1015', 'Captain',  '15 Oscar Cir',  5554015,15),
('Paula',  'Young',  'MD-1016', 'Sergeant', '16 Papa Way',   5554016,16),
('Quinn',  'Evans',  'MD-1017', 'Constable','17 Queen Rd',   5554017,17),
('Rosa',   'Lim',    'MD-1018', 'Lieutenant','18 Romeo Pkwy',5554018,18),
('Steve',  'George', 'MD-1019', 'Inspector','19 Sierra Ave', 5554019,19),
('Tina',   'Holt',   'MD-1020', 'Captain',  '20 Tango Dr',   5554020,20);

insert into incidents (incidentType, incidentDate, location, Description, status, VictimID, SuspectID) values
('Theft',     '2025-01-01 10:30:00', 'Central Market',       'Pickpocket in crowd',         'Open',    1000, 1000),
('Robbery',   '2025-01-05 21:00:00', 'North ATM',            'Armed robbery report',        'Open',    1001, 1001),
('Assault',   '2025-01-07 18:45:00', 'South Station',        'Altercation escalated',       'Closed',  1002, 1002),
('Vandalism', '2025-01-10 02:20:00', 'West Mall',            'Graffiti on walls',           'Open',    1003, 1003),
('Fraud',     '2025-01-12 15:15:00', 'Metro Bank',           'Fake check submitted',        'Under Investigation', 1004, 1004),
('Theft',     '2025-01-14 09:00:00', 'Library Lane',         'Laptop stolen from desk',     'Closed',  1005, 1005),
('Arson',     '2025-01-18 23:00:00', 'Warehouse 42',         'Fire reported',               'Closed',  1006, 1006),
('Mugging',   '2025-01-20 06:30:00', 'Park Gate',            'Handbag snatched',            'Open',    1007, 1007),
('Kidnapping','2025-01-21 22:00:00', 'Bus Terminal',         'Child missing report',        'Open',    1008, 1008),
('Assault',   '2025-01-25 01:45:00', 'Club District',        'Brawl among 3 people',        'Closed',  1009, 1009),
('Theft',     '2025-01-28 17:20:00', 'Market Lane',          'Wallet taken unnoticed',      'Open',    1010, 1010),
('Burglary',  '2025-01-30 03:15:00', 'Elm Apartments',       'Forced entry detected',       'Under Investigation', 1011, 1011),
('Theft',     '2025-02-01 12:00:00', 'Museum Lobby',         'Phone swiped',                'Closed',  1012, 1012),
('Extortion', '2025-02-04 16:40:00', 'Industrial Park',      'Threatening calls',           'Open',    1013, 1013),
('Arson',     '2025-02-07 05:50:00', 'Garage Alley',         'Fire set to car',             'Closed',  1014, 1014),
('Theft',     '2025-02-08 19:00:00', 'Cinema Hall',          'Bag missing post-show',       'Open',    1015, 1015),
('Robbery',   '2025-02-09 14:30:00', 'Bank Street',          'Armed entry reported',        'Open',     1019, 1019)
insert into incidents 
  (incidentType, incidentDate, location, Description, status, VictimID, SuspectID)
values
  ('Theft',    '2025-02-10 11:45:00', 'Mall Plaza',     'Wristwatch stolen from display case',        'Under Investigation', 1017, 1017),
  ('Burglary', '2025-02-11 03:30:00', 'Pine Street',    'Forced entry into residential home',         'Open',               1018, 1018),
  ('Assault',  '2025-02-12 23:15:00', 'Night Club',     'Bar fight left one patron injured',          'Closed',             1019, 1019);
  
 
insert into Evidence (EvidenceID, Description, Location_Found, incidentID) values
( 1, 'Fingerprint on recovered wallet',       'Central Market entrance',  1),
( 2, 'Surveillance footage clip',             'North ATM camera',         2),
( 3, 'Medical report of victim injuries',     'South Station lobby',      3),
( 4, 'Image of graffiti',                     'West Mall wall',           4),
( 5, 'Copy of forged check',                  'Metro Bank counter',       5),
( 6, 'Laptop sleeve',                         'Library desk',             6),
( 7, 'Burn pattern photograph',               'Warehouse 42',             7),
( 8, 'Clothing fiber sample',                 'Park Gate walkway',        8),
( 9, 'Security camera image',                 'Bus Terminal kiosk',       9),
(10, 'Video of altercation',                  'Club District entry',     10),
(11, 'Wallet clip',                           'Market Lane shop',        11),
(12, 'Force-entry tool mark',                 'Elm Apartments door',     12),
(13, 'Swiped phone record',                   'Museum Lobby',            13),
(14, 'Voicemail transcript',                  'Industrial Park office',  14),
(15, 'Charred key fragment',                  'Garage Alley car',        15),
(16, 'Theater camera footage',                'Cinema Hall screen',      16),
(17, 'Bank branch CCTV',                      'Bank Street foyer',       17),
(18, 'Surveillance recording',                'Mall Plaza kiosk',        18),
(19, 'Door pry-mark photo',                   'Pine Street residence',   19),
(20, 'Injury photo',                          'Night Club outside',      20);


insert into Reports (ReportID, incidentID, ReportingOfficer, ReportDate,    ReportDetails,                          Status) values
( 1,  1,  1, '2025-07-01 09:00:00','Initial victim statement recorded',         'Draft'),
( 2,  2,  2, '2025-07-02 10:30:00','Review of ATM footage',                     'In Review'),
( 3,  3,  3, '2025-07-03 14:20:00','Victim medical evaluation completed',        'Finalized'),
( 4,  4,  4, '2025-07-04 11:15:00','Graffiti samples collected',                'Draft'),
( 5,  5,  5, '2025-07-05 16:45:00','Bank staff interviewed',                    'In Review'),
( 6,  6,  6, '2025-07-06 13:10:00','Laptop ownership confirmed',                'Finalized'),
( 7,  7,  7, '2025-07-07 19:30:00','Arson witness statements obtained',         'Draft'),
( 8,  8,  8, '2025-07-08 08:50:00','Fiber analysis sent to lab',                'In Review'),
( 9,  9,  9, '2025-07-09 12:05:00','Camera malfunction noted',                  'Draft'),
(10, 10, 10, '2025-07-10 17:25:00','Altercation timeline established',          'Finalized'),
(11, 11, 11, '2025-07-11 09:45:00','Shop owner witness statement signed',       'In Review'),
(12, 12, 12, '2025-07-12 14:55:00','Entry point secured for forensic exam',     'Draft'),
(13, 13, 13, '2025-07-13 16:35:00','Phone record traced to suspect',            'Finalized'),
(14, 14, 14, '2025-07-14 10:15:00','Threat calls transcripted',                 'In Review'),
(15, 15, 15, '2025-07-15 11:05:00','Vehicle examination report filed',         'Draft'),
(16, 16, 16, '2025-07-16 18:40:00','CCTV synchronization complete',             'Finalized'),
(17, 17, 17, '2025-07-17 15:20:00','Fingerprint matches suspect',              'Finalized'),
(18, 18, 18, '2025-07-18 09:30:00','Retailer statements collected',             'In Review'),
(19, 19, 19, '2025-07-19 13:55:00','Forensic key analysis pending',             'Draft'),
(20, 20, 20, '2025-07-20 14:45:00','Injury severity report filed by paramedics','Finalized');

insert into cases (caseDescription, incidentID) values
  ('Pickpocket operation in the downtown market',          1),
  ('Undercover sting targeting robbery ring',               2),
  ('Follow-up residential burglary investigation',           3),
  ('Grand-theft auto—vehicle recovered',                    4),
  ('Hit-and-run investigation on Elm Street',               5),
  ('Suspected arson—warehouse fire',                        6),
  ('Cyber-fraud phishing scheme',                           7),
  ('Vandalism spree—graffiti cleanup',                      8),
  ('Assault at the city sports arena',                      9),
  ('Counterfeiting sting operation',                       10),
  ('Drug trafficking bust at the port',                    11),
  ('Money laundering network probe',                       12),
  ('Human trafficking ring dismantling',                   13),
  ('Weapon smuggling across the border',                   14),
  ('Public corruption scandal investigation',              15),
  ('Environmental crime—illegal toxic dumping',             16),
  ('Wildlife poaching crackdown',                          17),
  ('Illegal gambling den raid',                            18),
  ('Identity theft and financial fraud case',              19),
  ('Traffic violation investigation on Highway 50',        20);
  insert into  cases(caseDescription,incidentID) values('Violence against officer on Highway 50',20);

-- 20 incident location updates (incidentID 1–20)
update incidents set location = '13.0827,80.2707' where incidentID = 1;
update incidents set location = '13.0350,80.2440' where incidentID = 2;
update incidents set location = '13.0205,80.2498' where incidentID = 3;
update incidents set location = '13.0674,80.2376' where incidentID = 4;
update incidents set location = '13.0526,80.2530' where incidentID = 5;
update incidents set location = '13.0465,80.2337' where incidentID = 6;
update incidents set location = '13.0123,80.2095' where incidentID = 7;
update incidents set location = '13.1000,80.2800' where incidentID = 8;
update incidents set location = '13.0414,80.2376' where incidentID = 9;
update incidents set location = '13.0151,80.2124' where incidentID = 10;
update incidents set location = '13.0097,80.2200' where incidentID = 11;
update incidents set location = '13.0731,80.2376' where incidentID = 12;
update incidents set location = '13.0232,80.2101' where incidentID = 13;
update incidents set location = '13.0837,80.2690' where incidentID = 14;
update incidents set location = '13.0593,80.2675' where incidentID = 15;
update incidents set location = '13.0168,80.2279' where incidentID = 16;
update incidents set location = '13.0270,80.1999' where incidentID = 17;
update incidents set location = '13.0550,80.2300' where incidentID = 18;
update incidents set location = '13.0345,80.2189' where incidentID = 19;
update incidents set location = '13.0098,80.2059' where incidentID = 20;

-- 20 Evidence location updates (EvidenceID 1–20)
update Evidence set Location_Found = '13.0830,80.2710' where EvidenceID = 1;
update Evidence set Location_Found = '13.0353,80.2443' where EvidenceID = 2;
update Evidence set Location_Found = '13.0208,80.2501' where EvidenceID = 3;
update Evidence set Location_Found = '13.0677,80.2379' where EvidenceID = 4;
update Evidence set Location_Found = '13.0529,80.2533' where EvidenceID = 5;
update Evidence set Location_Found = '13.0468,80.2340' where EvidenceID = 6;
update Evidence set Location_Found = '13.0126,80.2098' where EvidenceID = 7;
update Evidence set Location_Found = '13.1003,80.2803' where EvidenceID = 8;
update Evidence set Location_Found = '13.0417,80.2379' where EvidenceID = 9;
update Evidence set Location_Found = '13.0154,80.2127' where EvidenceID = 10;
update Evidence set Location_Found = '13.0100,80.2203' where EvidenceID = 11;
update Evidence set Location_Found = '13.0734,80.2379' where EvidenceID = 12;
update Evidence set Location_Found = '13.0235,80.2104' where EvidenceID = 13;
update Evidence set Location_Found = '13.0840,80.2693' where EvidenceID = 14;
update Evidence set Location_Found = '13.0596,80.2678' where EvidenceID = 15;
update Evidence set Location_Found = '13.0171,80.2282' where EvidenceID = 16;
update Evidence set Location_Found = '13.0273,80.2002' where EvidenceID = 17;
update Evidence set Location_Found = '13.0553,80.2303' where EvidenceID = 18;
update Evidence set Location_Found = '13.0348,80.2192' where EvidenceID = 19;
update Evidence set Location_Found = '13.0101,80.2062' where EvidenceID = 20;

