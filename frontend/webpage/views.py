from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from webpage.models import data_collection

import sys 
import os 

#system path to extract.py and sentiment_analysis.py
#sys.path.append(os.path.abspath("C:/Users/Kbrowser123/Documents/GitHub/sentimentAnalysis_bot"))

#find directory of extract.py and sentiment_analysis.py
script_dir = os.path.dirname(os.path.abspath(__file__))

project_dir = os.path.abspath(os.path.join(script_dir, '..', '..'))

#set the path here
sys.path.append(project_dir)

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

        records = {
            "User Input" : result_data,
            "Extracted Words" : sentiment_result,
        }

        data_collection.insert_one(records)

        return render(request,"webpage/analyze.html",{"api_result": sentiment_result} )
    
    #if request doesn't succeed, go back to the input page
    else:
        return render(request, "webpage/analyze.html")

def group(request):
    return render(request, "webpage/group.html")



