import os
import platform

def get_archive_file_name_by_platform():
    sys = platform.system()
    arch = 'Unknown'

    if sys == 'Windows':
        arch = 'win32'
    elif sys == 'Linux':
        arch = 'linux64'
    elif sys == 'Darwin':
        arch = 'mac64'
        if platform.processor == 'arm':
            arch += '_m1'
    else:
        raise Exception('Failed to download chromedriver. Unknown OS.')
    
    return 'chromedriver_' + arch + '.zip'

def get_excutable_file_name_by_platform():
    sys = platform.system()

    if sys == 'Windows':
        return 'chromedriver.exe'
    else:
        return 'chromedriver'

def is_driver_excutable_file_exists():
    excutable_file_path = get_driver_excutable_file_path()
    if os.path.exists(excutable_file_path) == False:
        return False
    return True

def get_driver_excutable_file_path():
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.abspath(os.path.join(os.path.join(absolute_path, os.pardir), os.pardir))

    excutable_path = get_excutable_file_name_by_platform()
    return root_path + '/' + excutable_path
    