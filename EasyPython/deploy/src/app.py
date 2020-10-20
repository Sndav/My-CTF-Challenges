
from flask import Flask, escape, request
import pickle
import io
import sys

app = Flask(__name__)

class RestrictedUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        blackList = ["built","system","os","popen","read","pickle"]
        for b in blackList:
            if b in module or b in name:
                raise pickle.UnpicklingError("global '%s.%s' is forbidden" % (module, name))
        
        if module == '__main__' and (name == 'sys' or name == 'run' or name[:2] == '__'):
            return getattr(sys.modules['__main__'], name)
        raise pickle.UnpicklingError("global '%s.%s' is forbidden" % (module, name))


def restricted_loads(s):
    return RestrictedUnpickler(io.BytesIO(s)).load()

@app.route('/')
def index():
    return 'view source /src'

@app.route('/src')
def src():
    file = open("app.py").read()
    return file

@app.route('/pickle')
def NoVulnPickle():
    try:
        p = request.args.get("pickle")
        p = str(p)
        if "R" in p:
            return "hacker!"
        else:
            restricted_loads(p)
    except Exception as e:
        return "Failed"
    return "OK"

if __name__ == '__main__':
    app.run()
