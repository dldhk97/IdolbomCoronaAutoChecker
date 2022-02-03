from flask import Flask, render_template, request
from autochecker import checker
from datetime import datetime

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
    app.run(host='127.0.0.1', port=5000, debug=False)