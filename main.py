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
        capture_paper = False
        result_image = 'image/result.png'
        paper_image = ''

        if 'capture_paper' in request.form:
            capture_paper = True
            paper_image = 'image/paper_image.png'

        is_succeed, msg = checker.check(child_name, date, capture_paper)

        if not is_succeed:
            result_image = 'image/failed.jpg'

        return render_template('result.html', result_image=result_image, msg=msg, paper_image=paper_image)
    
    return render_template('index.html', date=date)

if __name__ == '__main__':
    app.run(host=SERVER_IP, port=SERVER_PORT, debug=False)