'''
Project: Patient Appointment Management System
Hospitals and clinics often need a simple way to manage patient appointments. In this project, you are required to develop a  that uses only lists and basic built-in Python functionalities to store, display, and delete patient appointments.

Objectives::

• To practice using Python  for storing and managing data.
• To apply  for interacting with the user.
• To demonstrate the use of  to organize code.
• To handle  such as adding, viewing, and deleting items from a list.


Requirements::

The program should provide a  where the user can:

• Add a new appointment (patient’s name, date, and time).
• Show all stored appointments in a clear and readable format.
• Delete an appointment by selecting its number from the list.
• Exit the program.


Appointments should be stored in a  as dictionaries or tuples containing:

• Patient name
• Appointment date
• Appointment time


The program must handle cases such as:

• Trying to view appointments when none exist.
• Attempting to delete an appointment when the list is empty.

Use only  (lists, loops, conditionals, and functions). No external libraries or databases are allowed.

'''

Appointments = []

def add_app():
   name = input("Enter patient name: ")
   date = input("Enter appointment date: ")
   time = input("Enter appointment time: ")
   appointment = {"name" : name, "date" : date, "time" : time}
   Appointments.append(appointment)
   print("✅ Appointment added successfully ")


def show_app():
    if len(Appointments) == 0:
        print("🫣 No appointments founded to show ")
    else :
        print("Appointments:")
        for i in range(0, len(Appointments)):
            print(f"{i+1}. The patient name : {Appointments[i]['name']} - Date: {Appointments[i]['date']} - Time: {Appointments[i]['time']} ")

def delete_app():
    if len(Appointments) == 0:
        print("🫣 No appointments founded to delete ")
    else :
        show_app()
        number = input("Enter appointment number from upper list to delete it : ")
        number = int(number)
        if number>0 and number<= len(Appointments):
            Appointments.pop(number-1)
            print("✅ appointment deleted successfully ")
        else:
             print("Invalid number")



while True:
    print ("\n🗓️💊 Patient Appointments Management Menu: ")
    print ("1. Add a new appointment")
    print ("2. Show appointments")
    print ("3. Delete appointment")
    print ("4. Exit")
    
    choice = input("Enter Your choice: ")
    
    if choice == "1":
        add_app()
    elif choice== "2":
        show_app()
    elif choice == "3":
        delete_app()
    elif choice == "4":
        print(" Goodbye 👋")
        break;
    else :
        print("Invalid choice")
        
        
        
        
        
        
        
