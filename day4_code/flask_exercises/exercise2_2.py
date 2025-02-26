from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template_string('''
        <!doctype html>
        <title>Current Time</title>
        <h1>The current time is: {{ current_time }}</h1>
    ''', current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)