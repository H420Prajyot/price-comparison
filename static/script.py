# script.py

def greet(name):
    print("Hello, World!")
    print("Hello, World!"+ name)


# script.py


import sys

if __name__ == '__main__':
    search_query = sys.argv[1]
    # Process the search query as needed
    # ...
    # Print the result or output that you want to send back to the Flask application
    print("Result:", search_query.upper())
    greet(search_query)

