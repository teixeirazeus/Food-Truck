import requests
from rich.console import Console
from rich.table import Table
import math
import emoji
import fire


# URL of your Django API
API_URL = "http://127.0.0.1:8000/food-trucks/"


class FoodTruckManager:
    """
    Manages food trucks.
    """

    def __init__(self, api_url):
        self.api_url = api_url
        self.food_trucks = self._fetch_food_trucks()
        self.search_results = []
        self.result_columns = [
            "Name",
            "Location",
            "Food Items",
        ]
        self.result_rows = ["applicant", "location_description", "food_items"]

    def _fetch_food_trucks(self):
        """Fetches food trucks from the API."""
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            return []

    def display_result(self):
        console = Console()
        table = Table(show_header=True, header_style="bold magenta", show_lines=True)

        for column in self.result_columns:
            table.add_column(column)

        for truck in self.search_results:
            row_data = [str(truck[row]) for row in self.result_rows]
            table.add_row(*row_data)

        console.print(table)

    def search_by_name(self, name, top=5):
        self.search_results = [
            truck
            for truck in self.food_trucks
            if name.lower() in truck["applicant"].lower()
        ][:top]

        self.display_result()

    def search_by_distance(self, user_lat, user_lon, top=5):
        # Calculate distance for each truck and add it to the truck data
        for truck in self.food_trucks:
            truck["distance"] = self._calculate_distance(
                user_lat, user_lon, truck["latitude"], truck["longitude"]
            )
            truck["distance"] = round(truck["distance"], 2)

        self.search_results = sorted(self.food_trucks, key=lambda x: x["distance"])[
            :top
        ]

        self.result_columns.append("Distance (km)")
        self.result_rows.append("distance")

        self.display_result()

    def search(self, name=None, latitude=None, longitude=None, top=5):
        if name:
            self.search_by_name(name, top)
        elif latitude is not None and longitude is not None:
            self.search_by_distance(float(latitude), float(longitude), top)
        else:
            print("Please provide either a name or latitude and longitude.")

    def _calculate_distance(self, lat1, lon1, lat2, lon2):
        # Convert latitude and longitude from degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = (
            math.sin(dlat / 2) ** 2
            + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        )
        c = 2 * math.asin(math.sqrt(a))
        r = 6371  # Radius of Earth in kilometers
        return c * r


def main():
    fire.Fire(
        {"search": FoodTruckManager(API_URL).search, "interactive": interactive_mode}
    )


def interactive_mode():
    food_truck_manager = FoodTruckManager(API_URL)

    while True:
        print(emoji.emojize(":fork_and_knife: Food Truck Finder :truck:"))
        print("1. Search by Name")
        print("2. Search by Location")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter food truck name: ")
            top = int(input("Enter the number of food trucks to display: "))
            food_truck_manager.search_by_name(name, top)
        elif choice == "2":
            user_lat = float(input("Enter your latitude: "))
            user_lon = float(input("Enter your longitude: "))
            top = int(input("Enter the number of food trucks to display: "))
            food_truck_manager.search_by_distance(user_lat, user_lon, top)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
