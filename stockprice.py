import requests
import json


api_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSCO.LON&outputsize=full&apikey=FVY8CIJ1H6JU2ZX3'
response = requests.get(api_url)

if response.status_code == 200:
    new_data = response.json()

    try:
        with open("tesco.json", "r") as json_file:
            existing_data = json.load(json_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        existing_data = []

        existing_data.append(new_data)

        with open("tesco.json", "w") as json_file:
            json.dump(existing_data, json_file, indent=4)
            print("Data appended to tesco.json file.")

else:
    print("Failed to retrieve data from the API. Status Code:", response.status_code)
