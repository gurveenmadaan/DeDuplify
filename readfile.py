def read_data(filename): #reads data from a file and returns it as a list of strings.
    # used for error handling
    try: 
        with open(filename, 'r') as file: #uses the with statement to open the specified file (filename) in read mode ('r'). The with statement is used here because it ensures that the file is properly closed, even if an exception is raised. 
            data = file.readlines() #reads all lines from the opened file and stores them as a list of strings. 
            data = [line.strip() for line in data] #strip() method is called to remove leading and trailing whitespace characters
            return data
    except FileNotFoundError: 
        print(f"File '{filename}' not found.") #prints an error message indicating that the specified file was not found. 
        return []