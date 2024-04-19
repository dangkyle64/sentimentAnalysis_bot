from extract import extract_
from sentiment_analysis import sentiment

def main():
    #extract text from file input / user input
    extract_text = extract_()
    text = extract_text.extract_words()
    
    #initalize sentiment analysis object with extracted text
    sentiment_analyze = sentiment(text)

    sentiment_analyze.sentiment_input()
    
    return 0

if __name__ == "__main__":
    main()