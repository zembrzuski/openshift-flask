from flask import Flask
app = Flask(__name__)

counter = 0

@app.route('/')
def hello_world():
    global counter
    counter = counter + 1
    return 'Flask Dockerized: {}'.format(counter)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

