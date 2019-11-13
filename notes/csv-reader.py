import csv
import os

with open('subjectinfo.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        sub = subject(
                subject_number = row['subject'],
                age = row['age'],
                gender = row['age'],
                height_cm = row['height/cm'],
                weight_kg = row['weight/kg']
                )
        sub.save()
