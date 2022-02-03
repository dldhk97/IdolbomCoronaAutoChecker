import os
from flask import Flask, render_template, request
from autochecker import checker
from datetime import datetime

SERVER_IP = os.environ.get('SERVER_IP')
SERVER_PORT = os.environ.get('SERVER_PORT')

app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route('/', methods=['POST', 'GET'])
def index():
    date = datetime.today().strftime('%Y.%m.%d')

    if request.method == 'POST':
        child_name = request.form['child_name']
        date = request.form['date']
        capture_screenshot = False
        image_file = 'image/no_screenshot.jpg'

        if 'capture_screenshot' in request.form:
            capture_screenshot = True
            image_file = 'image/result.png'

        msg = checker.check(child_name, date, capture_screenshot)

        return render_template('result.html', image_file=image_file, msg=msg)
    
    return render_template('index.html', date=date)

if __name__ == '__main__':
    app.run(host=SERVER_IP, port=SERVER_PORT, debug=False)