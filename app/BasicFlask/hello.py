from flask import Flask
app = Flask(__name__)

@app.route("/")
def bello():
    return "Hello World!"

@app.route('/hi/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/Welcome/<int:number>')
def hello_integer(number):
    return 'Hello %d!' % number

@app.route('/bello/<float:flo>')
def hello_float(flo):
    return 'Hello %f!' % flo


if __name__ == "__main__":
    app.run()
