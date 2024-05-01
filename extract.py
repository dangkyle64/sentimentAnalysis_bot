class extract_:

    def __init__(self):
        self.data = "text here for API"
    
    """
    Plan to extract the text here to make it easier for the API to read and to streamline requests into one method 
    """
    def extract_words(self, input_data):
        text = input_data
        print(text)
        
        """
        #implement a selection option between file reading and text reading
        stop = "continue"
        choice = input("Select input: file or user -> ")

        #Read text data from file
        while stop == "continue":
            
            #file input here
            if choice == "file":
                with open ("input.txt", "r", encoding = "utf-8") as file:
                    text = file.read()
                stop = input("If you wish to stop, put any other input than continue: ")

            #user input here
            elif choice == "user":
                text = input ("Please input a sentence: ")
                stop = input("If you wish to stop, put any other input than continue: ")

            #check if other choices are attempted after deciding to input
            else:
                print(f"This is not a valid choice between file or user")
                stop = "stopped"
        """
        

        #return as a string
        return text