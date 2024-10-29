import os
import django
import json


# Step 1: Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skin_diseases.settings')  # Replace with your project name
django.setup()

# Step 2: Import your Django model
from SkinDiseaseApp.models import SkinDisease
from HospitalApp.models import Hospital


# Step 3: Define the path to the JSON file


# Step 4: Load JSON data and save to database
def load_initial_data():
    json_file_path = 'diseases.json'

    # Read the JSON file
    with open(json_file_path, encoding='utf-8') as json_file:
        data = json.load(json_file)

        # Loop through each entry in the JSON array
        for entry in data:
            # Create and save a new DiseaseInfo instance
            SkinDisease.objects.create(
                name=entry['Disease'],
                disease_ar=entry['Disease_ar'],
                description=entry['Description'],
                symptoms=entry['Symptoms'],
                risk_factors=entry['Risks'],
                model_class_num=entry['model_class_num'],
                advices=entry['Advice'],
                read_more=entry['read_more']
            )

    print("Data loaded successfully!")


def load_hospitals_data():
    json_file_path: str = 'hospitals.json'

    with open(json_file_path, encoding='utf-8') as json_file:
        data = json.load(json_file)

        # Loop through each entry in the JSON array
        for entry in data:
            # Create and save a new DiseaseInfo instance
            Hospital.objects.create(
                name=entry['name'],
                address=entry['city'],
                city=entry['city'],
                contact_number=entry['contact_number'],
                lat=entry['coordinates']['latitude'],
                lon=entry['coordinates']['longitude'],

            )

    print("Hospitals Data loaded successfully!")


# Step 5: Execute the function when running the script
if __name__ == '__main__':
    # load_initial_data()
    load_hospitals_data()