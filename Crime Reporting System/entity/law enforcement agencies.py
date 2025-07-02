class Agency:
    def __init__(
        self,
        agency_id: int,
        agency_name: str,
        jurisdiction: str,
        contact_address: str,
        contact_phonenumber:int
    ):
        self.agency_id    = agency_id
        self.agency_name  = agency_name
        self.jurisdiction = jurisdiction
        self.contact_adress = contact_address
        self.contact_phonenumber = contact_phonenumber

    # — getters —
    def get_agency_id(self)    -> int:  return self.agency_id
    def get_agency_name(self)  -> str:  return self.agency_name
    def get_jurisdiction(self) -> str:  return self.jurisdiction
    def get_contact_address(self) -> str:  return self.contact_address
    def get_contact_phonenumber(self) -> int: return self.contact_phonenumber

    # — setters —
    def set_agency_id(self, agency_id: int):
        if not isinstance(agency_id, int):
            raise TypeError("agency_id must be int")
        self.agency_id = agency_id

    def set_agency_name(self, agency_name :str):
        if not isinstance(agency_name,str):
            raise TypeError("agency_name must be str")
        else:
            self.agency_name = agency_name

    def set_jurisdiction(self,jurisdiction : str):
        if not isinstance(jurisdiction,str):
            raise TypeError("jurisdiction must be str")
        else:
            self.jurisdiction =jurisdiction

    def set_contact_address(self, contact_address: str):
        if not isinstance(contact_address,str):
            raise TypeError("contact_address must be str")
        else:
            self.contact_address =contact_address

    def set_contact_phonenumber(self, contact_phonenumber: int):
        if not isinstance(contact_phonenumber, int):
            raise TypeError("contact_phonenumber must be int")
        else:
            self.contact_phonenumber = contact_phonenumber