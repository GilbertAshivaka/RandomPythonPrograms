#lists
students = ["Gilbert","Ann","Harry","Rose"]
for i in range (len(students)):
    print(i+1, students[i], sep="---")    

#Dictionaries 

students={
    "Gilbert":"Mombasa",
    "Ann":"Nairobi",
    "Harry":"Nakuru",
    "Rose":"Kisumu"
}


for student in students:
        print(student,students[student], sep="---")


#if the code included more data like this

students=[
    {"name":"Gilbert","city":"Mombasa","university":"Pwani"},
    {"name":"Ann","city":"Nairobi","university":"Zetech"},
    {"name":"Harry","city":"Nakuru","university":"Kemu"},
    {"name":"Rose","city":"Kisumu","university":"Maseno"},
   ]

for student in students:
      print(student["name"],student["city"],student["university"], sep="---")