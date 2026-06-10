from bs4 import BeautifulSoup
from peewee import SqliteDatabase, Model, CharField, IntegerField
import requests, time

db = SqliteDatabase("vehicles.db")

class Vehicle(Model):
    make = CharField()
    model = CharField()
    year = IntegerField()
    mpg = IntegerField()
    category = CharField()
    tco_10yr = IntegerField()

    class Meta:
        database = db

db.connect()
db.create_tables([Vehicle])

def get_fuel_data (year, make, model):
    
    if year < 1900 and year > 2100:
        print("Please enter a reasonable year.")
        
    base_url = "https://www.fueleconomy.gov/ws/rest/"
    base_headers = headers={"Accept":"application/json"}

    url = base_url + f"vehicle/menu/options?year={year}&make={make}&model={model}"
    response = requests.get(url, headers=base_headers)
    data = response.json()
    vehicle_id = data["menuItem"][0]["value"]

    if type(data["menuItem"]) == list:
        vehicle_id = data["menuItem"][0]["value"]
    else:
        vehicle_id = data["menuItem"]["value"]

    # second call to grab MPG for vehicle ID
    url = base_url + f"vehicle/{vehicle_id}"
    response = requests.get(url, headers=base_headers)
    data = response.json()

    return data["comb08"]

def get_maitenance_cost(make, model):

    base_url = "https://caredge.com/"
    base_headers = {"User-Agent": "Mozilla/5.0"}

    url = base_url + f"{make.lower()}/{model.lower()}/maintenance"
    response = requests.get(url, headers=base_headers)

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find_all("table")[0]
    total_maitenance = 0
    for row in table.find_all("tr")[1:]:
        cells = [td.get_text(strip=True) for td in row.find_all("td")]
        dollar_amount = cells[2]
        dollar_amount = dollar_amount.replace("$","")
        dollar_amount = dollar_amount.replace(",","")
        int_amount = int(dollar_amount)
        total_maitenance += int_amount
        
    return total_maitenance

def store_vehicle(data):
    existing = Vehicle.get_or_none(
        (Vehicle.make == data["make"]) &
        (Vehicle.model == data["model"]) &
        (Vehicle.year == data["year"])
        )
    
    if existing:
        print(f"Skipping {data['make']}")
        return
    
    Vehicle.create(**data)
    print(f"Stored {data['make']}")

list_of_vehicles = [
    {"year": 2020, "make": "Honda", "model": "Civic", "extra_text": " 4Dr", "category": "van"},
    {"year": 2020, "make": "Chevrolet", "model": "Blazer", "extra_text": " AWD", "category": "SUV"},
    {"year": 2021, "make": "Subaru", "model": "Outback", "extra_text": " AWD", "category": "SUV"}
]

for vehicle in list_of_vehicles:
    mpg = get_fuel_data(vehicle["year"], vehicle["make"], vehicle["model"]+vehicle["extra_text"])
    ten_year_maitenance = get_maitenance_cost(vehicle["make"], vehicle["model"])
    tco = (11000*10)/int(mpg)*4.50 + ten_year_maitenance
    if (int(mpg)) < 5:
        print("No MPG data.")

    print(f"{vehicle["year"]} {vehicle["make"]} {vehicle["model"]}{vehicle["extra_text"]}\nTCO: ${tco:.2f}")
    time.sleep(5)

    vehicle_data = {"make": vehicle["make"], "model": vehicle["model"], "year": vehicle["year"],
                    "mpg": mpg, "category": vehicle["category"], "tco_10yr": tco}
    store_vehicle(vehicle_data)

print("\n")

for v in Vehicle.select():
    print(v.make, v.model, v.tco_10yr)
