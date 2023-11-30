import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "food_truck_api.settings")
django.setup()

from trucks.models import FoodTruck
from django.core.exceptions import ValidationError
from django.utils.dateparse import parse_datetime


def load_data(csv_file_path):
    with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                if 0 in (float(row["Latitude"]), float(row["Longitude"])):
                    continue
                food_truck = FoodTruck(
                    location_id=row["locationid"],
                    applicant=row["Applicant"],
                    facility_type=row["FacilityType"],
                    location_description=row["LocationDescription"],
                    address=row["Address"],
                    blocklot=row["blocklot"],
                    block=row["block"],
                    lot=row["lot"],
                    food_items=row["FoodItems"],
                    latitude=float(row["Latitude"]),
                    longitude=float(row["Longitude"]),
                    zip_codes=int(row["Zip Codes"]) if row["Zip Codes"] else None,
                )
                food_truck.save()
            except ValidationError as e:
                print(f"Error saving food truck {row['Applicant']}: {e}")


if __name__ == "__main__":
    load_data("trucks/data/food-truck-data.csv")
