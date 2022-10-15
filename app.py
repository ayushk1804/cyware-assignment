from flask import Flask

IS_HEALTHY = True

app = Flask(__name__)

@app.route('/')
def hello_team():
    '''I know, its a simple program ;)'''
    return 'Hi Team'

@app.route('/health_check')
def health_check():
    if IS_HEALTHY:
        return "Healthy",200
    else:
        return "Unhealthy",502

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=15102)