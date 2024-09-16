from flask import flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/Bye/<name>')
def bye_name(name):
    return 'Bye %s!' % name

if __name__ == '__main__':
    app.run()
