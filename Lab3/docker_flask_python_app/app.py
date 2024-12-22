##from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Dockerized Flask!"

##if __name__ == '__main__':
    app.run(host='x.0.0.0', port5000)
