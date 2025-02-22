import requests
import csv

# Free API key (replace if necessary)
api_key = "6QULJW6WUQAKB2RI"
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={api_key}"
response = requests.get(url)

# Check if request worked
if response.status_code != 200:
    print(f"Error: API request failed with status {response.status_code}")
    print(response.text)
    exit()

data = response.json()

# Get latest price
latest_date = list(data["Time Series (Daily)"].keys())[0]
price = data["Time Series (Daily)"][latest_date]["4. close"]

# Save to CSV
with open("stock_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Stock", "Date", "Price"])
    writer.writerow(["IBM", latest_date, price])

print(f"IBM on {latest_date}: ${price}")