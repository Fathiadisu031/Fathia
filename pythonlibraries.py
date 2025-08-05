import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# array creation and sum

array = np.arange(10)
print(f" Mean : {array.mean()}")


data = pd.read_csv(r'c:\Users\Hp\Downloads\artists.csv')
data.head()
data.describe()

# fetching data from a public API
search = 'Rema'
response = requests.get(f'https://itunes.apple.com/search?term={search}&entity=song&limit=5')
if response.status_code == 200:
    data = response.json()
    for item in data['results']:
        print(f"Track Name: {item['trackName']}, Artist: {item['artistName']}")
else:
    print("Failed to fetch data from the API")
