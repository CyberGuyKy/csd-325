# Kyle Hughes
# CSD325
# Module 8.2 Assignment


import json

JSON_FILE = "Student.json"

def print_students(class_list):
    for student in class_list:
        print(f"{student['L_Name']}, {student['F_Name']}"
              f": ID = {student['Student_ID']} "
              f". Email = {student['Email']}")

with open(JSON_FILE, "r") as file:
    class_list = json.load(file)

print("=" * 55)
print("               ORIGINAL STUDENT LIST")
print("=" * 55)
print_students(class_list)
print()

new_student = {
    "F_Name": "Kyle",
    "L_Name": "Hughes",
    "Student_ID": 9000,
    "Email": "kyleiscool@fire.com"
}

class_list.append(new_student)

print("=" * 55)
print("           UPDATED STUDENT LIST")
print("=" * 55)
print_students(class_list)
print()

print("=" * 55)
choice = input("The student list has been updated.  Save Changes? (Y/N): ") .upper()

if choice == "Y":

    with open(JSON_FILE, "w") as file:
        json.dump(class_list, file, indent=4)

    print("=" * 55)
    print("        Student.json has been updated")
    print("=" * 55)

else:
    print("=" * 55)
    print("     Changes were not saved." )
    print("=" * 55)
