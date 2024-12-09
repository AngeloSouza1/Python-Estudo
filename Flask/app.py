from flask import Flask

app = Flask(__name__)

# localhost:5000/
@app.route('/')
def principal():
    return "<h2>Hello World</h2>"
