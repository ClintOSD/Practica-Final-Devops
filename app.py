from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola mundo desde Docker! Mi nombre es Clint Santana 2022-0023'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
