import requests 

url = 'https://api.meaningcloud.com/sentiment-2.1'

payload = {
    'key': 'put code here',
    'txt':'',
    'lang': 'en',
}

response = requests.post(url, data = payload)

print(f'Status code: {response.status_code}')
print(response.json())