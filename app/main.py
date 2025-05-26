from flask import Flask, render_template, request
from routes import handle_query
import os
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'))


@app.route('/', methods=['GET', 'POST'])
def home():
    response = ""
    if request.method == 'POST':
        user_input = request.form['query']
        response = handle_query(user_input)
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
