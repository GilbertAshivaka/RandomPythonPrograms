import csv
name = input("What is your name?  ")
school = input("Which school are you from?  ")

with open("students.csv","a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","school"])
    writer.writerow({"name":name,"school":school})









import csv
students =[]
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name":row["name"],"school":row["school"]})


for student in sorted(students, key= lambda student: student["name"]):
    print(f"{student['name']} is at {student['school']}")






