import os
from flask import Flask, render_template, request
from autochecker import checker
from datetime import datetime
from autochecker.driver.loader import load_driver

SERVER_IP = os.environ.get('SERVER_IP')
SERVER_PORT = os.environ.get('SERVER_PORT')

app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        child_name = request.form['child_name'].strip()
        date = request.form['date'].strip()
        capture_paper = False
        result_image = 'image/result.png'
        paper_image = ''

        if request.form['capture_paper'] == 'yyy':
            capture_paper = True
            paper_image = 'image/paper_image.png'

        is_succeed, result_msg, finish_msg = checker.check(child_name, date, capture_paper)
        info_msg = child_name + '(' + date + ')'

        if not is_succeed:
            result_image = 'image/failed.jpg'

        return render_template('result.html', result_image=result_image, result_msg=result_msg, info_msg=info_msg, finish_msg=finish_msg, paper_image=paper_image)
    
    return render_template('index.html', date=datetime.today().strftime('%Y.%m.%d'))

if __name__ == '__main__':
    load_driver(os.environ.get('CHROME_DRIVER_VERSION'))
    app.run(host=SERVER_IP, port=SERVER_PORT, debug=False)