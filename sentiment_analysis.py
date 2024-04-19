import requests 

#API Endpoint
url = 'https://api.meaningcloud.com/sentiment-2.1'

#Payload parameters 

payload = {
    'key': 'input key here',
    'lang': 'en',

}

#Read text data from file
with open ('input.txt', 'r', encoding = 'utf-8') as file:
    text = file.read()

#Include the 'txt' into the payload to be sent to the endpoint
payload['txt'] = text

#Define file input
files = {}

#Request to the API here
response = requests.post(url, data = payload, files = files)

print(f'Status code: {response.status_code}')
print(response.json())