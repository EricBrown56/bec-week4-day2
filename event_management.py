'''Problem Statement: Use the existing Event class by adding an instance attribute to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.'''

from helper import d

class Event:
        def __init__(self, name, date, participants=0):
            '''This method initializes the attributes of the Event class'''
            self.name = name
            self.date = date
            self.participants = participants

        def add_participant(self):
            '''This method increases the count of participants'''
            while True:
                try:
                    guests = int(input(f"How many guests are you bringing to the {self.name} including yourself? "))
                    self.participants += guests
                    print(f"{guests} guests have been added to the {self.name} event.")
                    break
                except TypeError:
                    print("Please enter a valid number.")
                    continue

        def get_participant_count(self):
            '''This method retrieves the current count of participants'''
            print(f"There are currently {self.participants} participants for the {self.name} event that is happening on {self.date}.")


# Create instances of the Event class and demonstrate adding participants. I ask for the number of guests the user is bringing to the event. I then add the number of guests to the participant count. I then print the number of participants for the event. I ask a second time to show that it adds the number of guests as a running total.

Birthday = Event('Birthday Party', '12/12/2024')
Wedding = Event('Wedding', '06/06/2025')
Graduation = Event('Graduation', '05/05/2026')
BabyShower = Event('Baby Shower', '07/07/2027')

Birthday.add_participant()
Birthday.get_participant_count()
Birthday.add_participant()
Birthday.get_participant_count()

d()

Wedding.add_participant()
Wedding.get_participant_count()
Wedding.add_participant()
Wedding.get_participant_count()

d()

Graduation.add_participant()
Graduation.get_participant_count()
Graduation.add_participant()
Graduation.get_participant_count()

d()

BabyShower.add_participant()
BabyShower.get_participant_count()
BabyShower.add_participant()
BabyShower.get_participant_count()