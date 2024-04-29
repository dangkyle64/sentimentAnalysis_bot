import requests 

#API Endpoint
url = 'https://api.meaningcloud.com/sentiment-2.1'

class sentiment:

    def __init__(self, text):
        self.text = text

    def sentiment_input(self):
        #Payload parameters 

        payload = {
            'key': '130c9b501c9c3e6cf8e2bd6fbd620019',
            'lang': 'en',

        }

        #Include the 'txt' into the payload to be sent to the endpoint
        payload['txt'] = self.text

        #Define file input
        files = {}

        #Request to the API here
        response = requests.post(url, data = payload, files = files)

        #Store .json file for use
        data = response.json()

        #print(f'Status code: {response.status_code}')
        #print(response.json())

        #Using specific keys to take out information 
        score = data["score_tag"]
        confidence = data["confidence"]

        #Access list from nested key in .json file
        sentence_list = data["sentence_list"]

        #Loop through each sentence dictionary
        for sentence in sentence_list:
            #Access score_tag, confidence, and text keys inside of sentence for use
            score2 = sentence["score_tag"]
            confidence2 = sentence["confidence"]
            input_statement = sentence["text"]

        print (f"The total sentiment score is {score} with a confidence of {confidence}")
        print (f"Specifically, input: {input_statement}. This has a score of {score2} and confidence of {confidence2}")
        return 0