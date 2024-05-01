from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

import sys 
import os 
sys.path.append(os.path.abspath("C:/Users/Kbrowser123/Documents/GitHub/sentimentAnalysis_bot"))
import extract
import sentiment_analysis


# Create your views here.
def home(request):
    return render(request, "webpage/home.html")

def analyze(request):
    if request.method == "POST":

        #get user input and then extract the words
        user_input = request.POST.get("text_input", "") #input form for user
        extract_result = extract.extract_()
        result_data = extract_result.extract_words(user_input)

        #initalize sentiment analysis object with extracted text
        sentiment_scan = sentiment_analysis.sentiment(result_data)
        sentiment_result = sentiment_scan.sentiment_input()
        print(sentiment_result)
        return render(request,"webpage/analyze.html",{"api_result": sentiment_result} )
    
    else:
        return render(request, "webpage/analyze.html")

def group(request):
    return render(request, "webpage/group.html")



