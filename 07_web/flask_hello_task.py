from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    return '''
    <p>Hello, Falsk!</p>
    <a href="/first">Go first</a>
    <p> </p>
    <a href="/second">Go second</a>
    '''

@app.route("/first")
def first():
    return '''
    <p>First Page</p>
    <a href="/">Go home</a>
    '''

@app.route("/second")
def second():
    return '''
    <p>Second Page</p>
    <a href="/">Go home</a>
    '''

if __name__ == "__main__":
     app.run(host="0.0.0.0")