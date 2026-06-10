"""
PIPELINE
- EPA API (real MPG and fuel cost)
- CarEdge Scrape
- Pandas (combine and clean)
- TCO Model (formula we design)
- Recommend (chart)
"""

import requests, time
from bs4 import BeautifulSoup

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

    print(data["comb08"])
    return data["comb08"]

# SCRAPING THE WEB

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

list_of_vehicles = [
    {"year": 2020, "make": "Honda", "model": "Civic", "extra_text": " 4Dr"},
    {"year": 2020, "make": "Chevrolet", "model": "Blazer", "extra_text": " AWD"},
    {"year": 2021, "make": "Subaru", "model": "Outback", "extra_text": " AWD"}
]

for vehicle in list_of_vehicles:
    mpg = get_fuel_data(vehicle["year"], vehicle["make"], vehicle["model"]+vehicle["extra_text"])
    ten_year_maitenance = get_maitenance_cost(vehicle["make"], vehicle["model"])
    tco = (11000*10)/int(mpg)*4.50 + ten_year_maitenance
    if (int(mpg)) < 5:
        print("No MPG data.")
    print(f"{vehicle["year"]} {vehicle["make"]} {vehicle["model"]}{vehicle["extra_text"]}\nTCO: ${tco:.2f}")
    time.sleep(5)

