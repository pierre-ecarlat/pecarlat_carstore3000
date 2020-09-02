from flask import Flask, render_template, redirect
from .forms import PreferencesForm

app = Flask(__name__)

# Config options
app.config.from_object('config')

from .models import Car

@app.route('/', methods=['GET', 'POST'])
def contact():
    form = PreferencesForm()
    if form.validate_on_submit():
        print(form.fuel_type.data)
        return render_template('results.html')
    return render_template('preferences.html', form=form)