import output as output
from flask import Flask, render_template , request
import subprocess
from static.script import greet  # Import the necessary function from price_comparison.py


app = Flask(__name__)

@app.route('/')
def index():
    # Execute the Python file and capture the output
     # = subprocess.check_output(['python', 'static/script.py']).decode('utf-8')


    return render_template('index.html')

# @app.route('/search', methods=['POST'])
# def search():
#     # Get the input from the search bar
#     search_query = request.form['search_query']
#
#     # Pass the input to the Python file for further processing
#     proccess = subprocess.Popen(['python', 'script.py', search_query], stdout=subprocess.PIPE)
#     output, _ = process.communicate()
#
#     return render_template('index.html', output=output)



@app.route('/search', methods=['GET','POST'])
def search():
    search_query = request.form['search_query']

    # Execute the Python script with search_query as a command-line argument
    result = subprocess.run(['python', 'static/price_comparator.py', search_query], capture_output=True, text=True)

    # Get the output from the Python script
    output = result.stdout.strip()
    # output = result.stdout.strip()

    return render_template('pass.html', name=output)
# def search():
#     search_query = request.args.get('search_query')
#
#     # Perform the search using the find function
#     result = greet(search_query)
#
#     # Return the result as a response
#     return render_template('pass.html', name=result)


if __name__ == '__main__':
    app.run(debug=True)
