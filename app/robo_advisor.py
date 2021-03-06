## TO DO
# to usd equation
# date accessed 


import csv
import requests
import os
import json

# DESCROPTION
def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

#
# INFO INPUTS
#

requests_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"

response = requests.get(requests_url)
# print(type(response)) #> <class 'requests.models.Response'>
# print(response.status_code) #> 200
# print(response.text) 

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
tsd = parsed_response["Time Series (Daily)"]


dates = list(tsd.keys()) # TODO: sort to ensure latest day is first
latest_day = dates[0]

latest_close = tsd[latest_day]["4. close"]


# get high price from each day
high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    low_price = tsd[date]["3. low"]
    high_prices.append(float(high_price))
    low_prices.append(float(low_price))

# maximum of all high prices
recent_high = max(high_prices)
recent_low = min(low_prices)

#breakpoint()



#
# INFO OUTPUTS
#


csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp","open","high","low","close","volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    
    # looping
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"]
            })
    


print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm") # date time module OYO
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!") # TODO using inputs created for high and low?
print("RECOMMENDATION REASON: TODO") # TODO using inputs created for high and low?
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}") 
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")


#csv_file_path = "data/prices.csv" # a relative filepath

# csv_file_path = "data/prices.csv" # a relative filepath



