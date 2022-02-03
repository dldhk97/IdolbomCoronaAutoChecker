from datetime import datetime

def print_log(message):
    now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    
    print('[' + now + '] ' + str(message))