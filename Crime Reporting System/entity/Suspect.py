from datetime import date

class Suspect:
    def __init__(
        self,
        suspect_id: int=None,
        first_name: str=None,
        last_name: str=None,
        date_of_birth: date=None,
        gender: str=None,
        address: str=None,
        phone_number: str=None
    ):
        self.suspect_id    = suspect_id
        self.first_name    = first_name
        self.last_name     = last_name
        self.date_of_birth = date_of_birth
        self.gender        = gender
        self.address       = address
        self.phone_number  = phone_number

    # — getters —
    def get_suspect_id(self):
        return self.suspect_id
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_date_of_birth(self) :
        return self.date_of_birth
    def get_gender(self):
        return self.gender
    def get_address(self):
        return self.address
    def get_phone_number(self):
        return self.phone_number

    # — setters —
    def set_victim_id(self, victim_id):
        if not isinstance(victim_id, int):
            raise TypeError("victim_id must be int")
        else:
            self.victim_id = victim_id

    def set_first_name(self, first_name: str):
        if not isinstance(first_name, str):
            raise TypeError("first_name must be str")
        else:
         self.first_name = first_name

    def set_last_name(self, last_name: str):
        if not isinstance(last_name, str):
            raise TypeError("last_name must be str")
        else:
         self.last_name = last_name

    def set_date_of_birth(self, date_of_birth: date):
        if not isinstance(date_of_birth, date):
            raise TypeError("date_of_birth must be date")
        else:
         self.date_of_birth = date_of_birth

    def set_gender(self, gender: str):
        if not isinstance(gender, str):
            raise TypeError("gender must be str")
        else:
         self.gender =gender

    def set_address(self, address: str):
        if not isinstance(address, str):
            raise TypeError("address must be str")
        else:
            self.address = address

    def set_phone_number(self, phone_number: str):
        if not isinstance(phone_number, str):
            raise TypeError("phone_number must be str")
        else:
            self.phone_number = phone_number