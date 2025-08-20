
'''
Write a program to display all employee names and their departments.

employees = {
    "E001": {"name": "Alice", "department": "Finance"},
    "E002": {"name": "Bob", "department": "IT"},
    "E003": {"name": "Charlie", "department": "HR"}
}

'''

employees = {
    "E001": {"name": "Alice", "department": "Finance"},
    "E002": {"name": "Bob", "department": "IT"},
    "E003": {"name": "Charlie", "department": "HR"}
}


for key,value in employees.items():

    if isinstance(value,dict):
        print(key, value["name"].ljust(12),value["department"])
    print()