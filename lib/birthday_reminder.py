class Birthday():

    def __init__(self):
        self.birth_dict = {}

    def add(self, name, date):
        self.birth_dict[name] = date

    def change_date(self, name, new_date):
        self.birth_dict[name] = new_date