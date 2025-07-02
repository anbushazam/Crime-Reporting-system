# entity/officer.py
class officer:
    def __init__(self,officerID:int,firstName:str, lastName:str,
                 badgeNumber,
                 rank,
                Contact_address,
                 Contact_phonenumber: int,
                 agencyID):
        self.officerID  = officerID
        self.firstName = firstName
        self.lastName  = lastName
        self.badgeNumber  = badgeNumber
        self.rank  = rank
        self.Contact_address= Contact_address
        self.Contact_phonenumber=Contact_phonenumber
        self.agencyID  = agencyID

    # getters
    def getOfficerID(self):          return self.officerID
    def getFirstName(self):          return self.firstName
    def getLastName(self):           return self.lastName
    def getBadgeNumber(self):        return self.badgeNumber
    def getRank(self):               return self.rank
    def getContact_address(self): return self.Contactaddress
    def getContact_phonenumber(self): return self.Contact_phonenumber
    def getAgencyID(self):           return self.agencyID

    # setters
    def set_OfficerID(self, officerID):
        if not isinstance(officerID, int):
            raise TypeError("officerID must be an integer")
        self.officerID = officerID

    def set_FirstName(self, firstName):
        if not isinstance(firstName, str):
            raise TypeError("firstName must be a string")
        self.firstName = firstName

    def set_LastName(self, lastName):
        if not isinstance(lastName, str):
            raise TypeError("lastName must be a string")
        self.lastName = lastName

    def set_BadgeNumber(self, badgeNumber):
        if not isinstance(badgeNumber, str):
            raise TypeError("badgeNumber must be a string")
        self.badgeNumber = badgeNumber

    def set_Rank(self, rank):
        if not isinstance(rank, str):
            raise TypeError("rank must be a string")
        self.rank = rank

    def set_Contact_address(self, Contact_address):
        if not isinstance(Contact_address, str):
            raise TypeError("contact_address must be a string")
        self.Contact_address = Contact_address

    def set_Contact_phonenumber(self, Contact_phonenumber):
        if not isinstance(Contact_phonenumber, int):
            raise TypeError("Contact_phonenumber must be a int")
        self.Contact_phonenumber = Contact_phonenumber


    def set_AgencyID(self, agencyID):
        if not isinstance(agencyID, int):
            raise TypeError("agencyID must be an integer")
        self.agencyID = agencyID