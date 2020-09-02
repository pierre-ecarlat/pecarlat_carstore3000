from flask import Flask, render_template

app = Flask(__name__)

# Config options
app.config.from_object('config')

@app.route('/')
def index():
    #print(Car.query.all())
    return render_template('index.html')