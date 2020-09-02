from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PreferencesForm(FlaskForm):
    """Preferences of the user.
    """
    fuel_type = StringField('Fuel type', [DataRequired()])
    transmisison = StringField('Transmission', [DataRequired()])
    color = StringField('Color', [DataRequired()])
    submit = SubmitField('Submit')