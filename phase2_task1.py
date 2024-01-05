#!/usr/bin/env python
# coding: utf-8

# In[3]:


def add_record(records, employee_id, name, position, salary):
    record = {}
    record['name'] = name
    record['position'] = position
    record['salary'] = salary
    records[employee_id] = record

def remove_record(records, employee_id):
    if employee_id in records:
        del records[employee_id]
        print(f"Record for employee ID {employee_id} is removed.")
    else:
        print(f"No record found for employee ID {employee_id}.")

def update_record(records, employee_id, name=None, position=None, salary=None):
    if employee_id in records:
        record = records[employee_id]
        if name:
            record['name'] = name
        if position:
            record['position'] = position
        if salary:
            record['salary'] = salary
        print(f"Record for employee ID {employee_id} is updated.")
    else:
        print(f"No record found for employee ID {employee_id}.")

def display_record(records, employee_id):
    if employee_id in records:
        record = records[employee_id]
        print(f"Employee ID: {employee_id}")
        print(f"Name: {record['name']}")
        print(f"Position: {record['position']}")
        print(f"Salary: ${record['salary']}")
    else:
        print(f"No record found for employee ID {employee_id}.")

def display_all_records(records):
    if records:
        for employee_id, record in records.items():
            print(f"Employee ID: {employee_id}")
            print(f"Name: {record['name']}")
            print(f"Position: {record['position']}")
            print(f"Salary: ${record['salary']}")
            print("---------------------")
    else:
        print("No records found.")

employee_records = {}

while True:
    print("\nEmployee Records Menu:")
    print("1. Add a record")
    print("2. Update a record")
    print("3. Remove a record")
    print("4. Display a record")
    print("5. Display all records")
    print("6. Quit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        employee_id = input("Enter employee ID: ")
        name = input("Enter name: ")
        position = input("Enter position: ")
        salary = input("Enter salary: ")
        add_record(employee_records, employee_id, name, position, salary)

    elif choice == '2':
        employee_id = input("Enter employee ID to update: ")
        name = input("Enter updated name (or press Enter to skip): ")
        position = input("Enter updated position (or press Enter to skip): ")
        salary = input("Enter updated salary (or press Enter to skip): ")
        update_record(employee_records, employee_id, name, position, salary)

    elif choice == '3':
        employee_id = input("Enter employee ID to remove: ")
        remove_record(employee_records, employee_id)

    elif choice == '4':
        employee_id = input("Enter employee ID to display: ")
        display_record(employee_records, employee_id)

    elif choice == '5':
        display_all_records(employee_records)

    elif choice == '6':
        break

    else:
        print("Invalid choice. Please try again.")

print("Program ended.")


# In[ ]:





# In[ ]:





# In[ ]:




