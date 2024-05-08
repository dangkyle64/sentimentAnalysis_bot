from django.shortcuts import render
import requests

def api_call(user_input):
    url = 'https://api.meaningcloud.com/sentiment-2.1'
    params = {'txt': user_input, 'key': '130c9b501c9c3e6cf8e2bd6fbd620019', 'lang': 'en'} 
    try:
        response = requests.post(url, data=params)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API call failed: {e}")
        return {} 

def format_api_result(api_result):
    if 'status' in api_result and api_result['status']['code'] != "0":
        print("API Error:", api_result['status']['msg'])
        return {}

    return {
        'overall_sentiment': api_result.get('score_tag', 'Unknown'),
        'confidence': api_result.get('confidence', '0'),
        'irony': api_result.get('irony', 'Unknown'),
        'sentences': [
            {'text': sentence['text'], 'sentiment': sentence.get('score_tag', 'N/A')}
            for sentence in api_result.get('sentence_list', [])
        ],
        'key_concepts': [
            {'text': concept.get('form', ''), 'type': concept.get('type', 'N/A')}
            for concept in api_result.get('sentimented_concept_list', [])
        ]
    }

def analyze(request):
    if request.method == "POST":
        user_input = request.POST.get("text_input", "")
        api_result = api_call(user_input) 
        formatted_result = format_api_result(api_result)
        return render(request, "webpage/analyze.html", {"api_result": formatted_result})
    else:
        return render(request, "webpage/analyze.html")

def home(request):
    return render(request, "webpage/home.html")

def group(request):
    return render(request, "webpage/group.html")
