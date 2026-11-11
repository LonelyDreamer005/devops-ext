from flask import Flask
app = Flask(__name__)

def add(a,b):
    return a + b
def sub(a, b):
    return a - b
def mul(a,b):
    return a * b

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)