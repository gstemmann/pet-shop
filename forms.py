from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional


species = ['dog', 'cat', 'turtle', 'frog', 'bear',
            'dragon', 'snake', 'horse', 'rooster', 'goat', 'pig', 'rat',
            'rabbit']

class AnimalForm(FlaskForm):
    name = StringField("Pet name", validators=[
                       InputRequired(message="Name cannot be blank")])
    species = SelectField('Species', choices=[(sp, sp) for sp in species])
    available = BooleanField("This is animal is available")
