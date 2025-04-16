from faker import Faker
import csv
from random import choice, randint

# Initialize Faker
fake = Faker()

# Define possible values for certain fields
branches = ['Engineering', 'Science', 'Arts']
levels = ['Undergraduate', 'TVET', 'Postgraduate', 'PhD']
current_year = 2025
years = list(range(current_year - 10, current_year + 1))

# Function to generate a student record
def generate_student():
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    phone = fake.phone_number()
    admission_no = str(randint(100000, 999999))
    branch = choice(branches)
    enrollment_year = choice(years)
    level = choice(levels)
    
    return [
        first_name,
        last_name,
        email,
        phone,
        admission_no,
        branch,
        enrollment_year,
        level
    ]

# Write to CSV file
with open('studentData.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write header
    writer.writerow([
        'First Name',
        'Last Name',
        'Email',
        'Phone',
        'Admission No',
        'Branch',
        'Enrollment Year',
        'Level'
    ])
    
    # Generate and write 1000 records
    for _ in range(1000):
        writer.writerow(generate_student())

print("Generated studentData.csv with 1000 records")
