class extract_:

    def __init__(self):
        self.data = "text here for API"
    
    """
    Plan to extract the text here to make it easier for the API to read and to streamline requests into one method 
    """
    def extract_words():

        #implement a selection option between file reading and text reading
        
        #Read text data from file
        with open ('input.txt', 'r', encoding = 'utf-8') as file:
            text = file.read()

        #implement text reading 

        #return as a string
        return text