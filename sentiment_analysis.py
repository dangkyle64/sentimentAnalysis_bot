import requests 

#API Endpoint
url = 'https://api.meaningcloud.com/sentiment-2.1'

class sentiment:

    def __init__(self, text):
        self.text = ''

    def sentiment_input(self):
        #Payload parameters 

        payload = {
            'key': 'input key here',
            'lang': 'en',

        }

        #Include the 'txt' into the payload to be sent to the endpoint
        payload['txt'] = self.text

        #Define file input
        files = {}

        #Request to the API here
        response = requests.post(url, data = payload, files = files)

        print(f'Status code: {response.status_code}')
        print(response.json())

        return 0