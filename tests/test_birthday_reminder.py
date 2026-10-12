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

def test_change_name():
    birthday = Birthday()
    birthday.add("Bob", "2002-02-28")
    birthday.add("Dave", "2010-12-03")
    birthday.add("John", "1999-11-20")
    birthday.change_name("Dave", "Paul")
    assert birthday.birth_dict == {"Bob": "2002-02-28", "Paul": "2010-12-03", "John": "1999-11-20"}

def test_list_upcoming_birthdates():
    birthday = Birthday()
    birthday.add("Bob", "2002-02-28")
    birthday.add("Dave", "2010-12-03")
    birthday.add("John", "1999-11-20")
    assert birthday.list_upcoming_birthdates() == ["John", "Dave", "Bob"]

def test_upcoming_ages():
    birthday = Birthday()
    birthday.add("Bob", "2002-02-28")
    birthday.add("Dave", "2010-12-03")
    birthday.add("John", "1999-11-20")
    assert birthday.upcoming_ages() == {"Bob": 25, "Dave": 16, "John": 27}