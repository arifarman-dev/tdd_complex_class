from datetime import datetime

class Birthday():

    def __init__(self):
        self.birth_dict = {}

    def add(self, name, date):
        self.birth_dict[name] = date

    def change_date(self, name, new_date):
        self.birth_dict[name] = new_date

    def change_name(self, old_name, new_name):
        if old_name in self.birth_dict:
            self.birth_dict[new_name] = self.birth_dict.pop(old_name)

    def list_upcoming_birthdates(self):
        birth_list = []
        birth_dict = {}
        today = datetime.today().date()
        for name, date in self.birth_dict.items():
            birthdate = datetime.strptime(date, "%Y-%m-%d").date()
            this_year_birthday = birthdate.replace(year=today.year)
            difference = (this_year_birthday - today).days
            if difference < 0:
                difference += 365
            birth_list.append(difference)
            birth_dict[name] = difference
        sorted_list = sorted(birth_list)
        return_list = []
        for difference in sorted_list:
            for key, value in birth_dict.items():
                if value == difference:
                    return_list.append(key)
        return return_list

    def upcoming_ages(self):
        today = datetime.today().date()
        birth_dict = {}
        for name, date in self.birth_dict.items():
            birthdate = datetime.strptime(date, "%Y-%m-%d").date()
            birthyear = birthdate.year
            birthmonth = birthdate.month
            birthday = birthdate.day
            if birthmonth < today.month:
                next_birthday = today.year + 1 - birthyear
            elif birthmonth == today.month:
                if birthday > today.day:
                    next_birthday = today.year - birthyear
                else: 
                    next_birthday = today.year + 1 - birthyear
            else:    
                next_birthday = today.year - birthyear
            birth_dict[name] = next_birthday
        return birth_dict
            


