from lib.birthday_reminder import *

def test_adding_birthdates():
    birthday = Birthday()
    birthday.add("Bob", "2002-02-28")
    birthday.add("Dave", "2010-12-03")
    birthday.add("John", "1999-11-20")
    assert birthday.birth_dict == {"Bob": "2002-02-28", "Dave": "2010-12-03", "John": "1999-11-20"}

def test_update_date_of_birth():
    birthday = Birthday()
    birthday.add("Bob", "2002-02-28")
    birthday.add("Dave", "2010-12-03")
    birthday.add("John", "1999-11-20")
    birthday.change_date("Bob", "2003-02-28")
    assert birthday.birth_dict == {"Bob": "2003-02-28", "Dave": "2010-12-03", "John": "1999-11-20"}
