import requests
import csv

# Free API key (demo key, replace if it fails)
api_key = "2d3cd0274ebcfb26588412cf8c950330"
url = f"http://api.openweathermap.org/data/2.5/weather?q=San%20Francisco&appid={api_key}&units=imperial"
response = requests.get(url)

# Check if request worked
if response.status_code != 200:
    print(f"Error: API request failed with status {response.status_code}")
    print(response.text)
    exit()

data = response.json()

# Extract city and temp
city = data["name"]
temp = data["main"]["temp"]

# Save to CSV
with open("weather_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["City", "Temperature"])
    writer.writerow([city, f"{temp}°F"])

print(f"Scraped {city}: {temp}°F")