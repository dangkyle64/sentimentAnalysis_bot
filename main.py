from extract import extract_
from sentiment_analysis import sentiment
from mongo import mongo_

def main():
    #extract text from file input / user input
    #mongo_.insertData("now", "working")
    extract_text = extract_()
    text = extract_text.extract_words()
    
    
    #initalize sentiment analysis object with extracted text
    sentiment_analyze = sentiment(text)

    output = sentiment_analyze.sentiment_input()
    mongo_.insertData(text, output)
    
    
    return 0

if __name__ == "__main__":
    main()