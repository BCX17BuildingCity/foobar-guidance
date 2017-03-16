import subprocess
from bottle import run, post, request, response, get, route
import json,requests

@route('/<path>',method = 'POST')
def process(path):
    return subprocess.check_output(['python',path+'.py'],shell=True)

run(host='localhost', port=8080, debug=True)
