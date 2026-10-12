# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Birthday:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   dictionary: dictionary of names and birthdays
        # Side effects:
        #   empty dictionary
        pass # No code here yet

    def add(self, name, date):
        # Parameters:
        #   name: string representing a person
        #   date: the persons date of birth
        # Returns:
        #   Nothing
        # Side-effects
        #   adds name and date of birth to the dictionary
        pass # No code here yet

    def change_date(self, name, new_date):
        # Parameters:
        #   name: string representing a person
        #   new_date: the persons date of birth
        # Returns:
        #   nothing
        # Side-effects:
        #   updates the date of birth for that name
        pass # No code here yet
    
    def change_name(self, old_name, new_name):
        # Parameters:
        #   old_name: string representing a person
        #   new_name: string representing a person
        # Returns:
        #   nothing
        # Side-effects:
        #   changes the old name to the new name
        pass
    
    def list_upcoming_birthdates(self):
        # Returns:
        #   returns a list of peoples names in order of their birthdays
        # Side-effects:
        #   no side effects
    
    def upcoming_ages(self):
        # Returns:
        #   returns a dictionary of friends and their upcoming ages
        # Side-effects:
        #   no side effects
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a name and date of birth
Dictionary is updated with the information
"""
birthday = Birthday()
birthday.add("Bob": "2002-02-28")
birthday.add("Dave": "2010-12-03")
birthday.add("John": "1999-11-20")

"""
Given a name and new date
Dictionary is updated with new date of birth
"""

birthday = Birthday()
birthday.add("Bob": "2002-02-28")
birthday.change_date("Bob", "2003-02-28")

"""
Given a an old name and a new name
Dictionary is updated with the new name
"""

birthday = Birthday()
birthday.add("Dave": "2010-12-03")
birthday.change_name("Dave", "Paul")

"""
Return a list of friends with upcoming birthdays
"""
birthday = Birthday()
birthday.add("Bob": "2002-02-28")
birthday.add("Dave": "2010-12-03")
birthday.add("John": "1999-11-20")
birthday.list_upcoming_birthdates() # => list in order of latest birthdates

"""
Return a dictionary of friends and their upcoming age
"""
birthday = Birthday()
birthday.add("Bob": "2002-02-28")
birthday.add("Dave": "2010-12-03")
birthday.add("John": "1999-11-20")
birthday.upcoming_ages() # => dictionary of names and their ages upcoming ages

"""
Given an empty birthday or an empty name
"""
birthday = Birthday()
birthday.add("Bob") # => return input age
birthday.add("2002-02-28") # => you must enter name first followed by birthdate

"""
Given an old name but no new name
"""
birthday = Birthday()
birthday.add("Dave": "2010-12-03")
birthday.change_name("Dave") # => you must enter a new name to update the old one

"""
Given a non existant old name
"""
birthday = Birthday()
birthday.change_name("Paul") # => person does not exist in dictionary
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
