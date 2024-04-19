from extract import extract_
from sentiment_analysis import sentiment

def main():
    #extract text from file input / user input
    extract_text = extract_()

    #initalize sentiment analysis object with extracted text
    sentiment_analyze = sentiment(extract_text)

    sentiment_analyze.sentiment_input()
    
    return 0

if __name__ == "__main__":
    main()