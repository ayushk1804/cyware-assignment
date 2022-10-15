from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_team():
    '''I know, its a simple program ;)'''
    return 'Hi Team'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)