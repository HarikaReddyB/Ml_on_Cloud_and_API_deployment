import requests
import json

url = 'http://localhost:5000/predict'

# Sample data for prediction
data = {'area': 2000, 'bedrooms': 3, 'age': 10}

# Converting the data to JSON format
json_data = json.dumps(data)
response = requests.post(url, json=json_data)

# Printing the response received from the API 
print(response.json())

