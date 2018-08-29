# encoding: utf-8
import platform
import subprocess
import os
import sys
try:
    input_func = raw_input
except NameError:
    input_func = input
try:
    import urllib.request as urllib_request  # for Python 3
except ImportError:
    import urllib2 as urllib_request  # for Python 2


def download_snappy(py_ver, bit):
    base_url = r'http://www.quantos.org/downloads/snappy/'
    snappy_file = dict()
    snappy_file['py2.7-32bit'] = 'python_snappy-0.5.1-cp27-cp27m-win32.whl'
    snappy_file['py2.7-64bit'] = 'python_snappy-0.5.1-cp27-cp27m-win_amd64.whl' 
    snappy_file['py3.4-32bit'] = 'python_snappy-0.5.1-cp34-cp34m-win32.whl'
    snappy_file['py3.4-64bit'] = 'python_snappy-0.5.1-cp34-cp34m-win_amd64.whl' 
    snappy_file['py3.5-32bit'] = 'python_snappy-0.5.1-cp35-cp35m-win32.whl'
    snappy_file['py3.5-64bit'] = 'python_snappy-0.5.1-cp35-cp35m-win_amd64.whl' 
    snappy_file['py3.6-32bit'] = 'python_snappy-0.5.1-cp36-cp36m-win32.whl'
    snappy_file['py3.6-64bit'] = 'python_snappy-0.5.1-cp36-cp36m-win_amd64.whl' 

    key = 'py' + py_ver + "-" + bit
    file_name = snappy_file[key]
    url = base_url + file_name
    
    req  = urllib_request.Request(url)
    rep = urllib_request.urlopen(req)
    body = rep.read()

    with open(file_name, 'wb') as f:
        f.write(body)
        f.close()
    return file_name


def decode_if_possible(b, encoding='utf-8'):
    if b is not None and hasattr(b, 'decode'):
        return b.decode(encoding)


def exec_cmd(command):
    p = subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=1)
    while True:
        line = p.stdout.readline()
        if not line:
            break
        print(line)
    p.wait()


def pip_install(name):
    cmd = 'pip install ' + name
    exec_cmd(cmd)


def main():
    SUPPORTTED_PYTHON_VERSIONS = ('2.7', '3.4', '3.5', '3.6')
    PACKAGE_NAME = 'finxos'
    MASTER_BRANCH = 'https://github.com/PKUJohnson/finxos/archive/master.zip'

    print("\nDetecting Python version...")
    py_major_ver, py_minor_ver, py_patch_ver = platform.python_version_tuple()
    py_ver = '.'.join([py_major_ver, py_minor_ver])
    if py_ver not in SUPPORTTED_PYTHON_VERSIONS:
        print("Unsupported Python version: {}".format(py_ver))
        return -1
    print("Python version: {}".format(py_ver))

    print("\nDetecting System version...")
    bit, system = platform.architecture()
    print("System version: {} {}".format(bit, system))
    
    print("\nDownloading python-snappy from server...")
    file_name = download_snappy(py_ver, bit)
    print("Download complete.")

    print("\nInstalling python-snappy...")
    pip_install(file_name)
    print("Install complete.")

    print("\nInstalling finxos...")
    correct_input = False
    while not correct_input:
        user_input = input_func("Input 1 for stable version; 2 for latest version:\n")
        if user_input == '1':
            pip_install(PACKAGE_NAME)
            correct_input = True
        elif user_input == '2':
            print("Start to download latest version from GitHub and instlall it. This may take several minutes...")
            pip_install(MASTER_BRANCH)
            correct_input = True
    print("Install complete.")  


if __name__ == "__main__":
    main()
