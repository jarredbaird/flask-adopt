
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class PetForm(FlaskForm):
    name = StringField("Name", 
                       validators=[InputRequired(message="Pet needs a name!")])
    species = SelectField("Species")
    photo_url = StringField("Photo")

    age = IntegerField("Age in years")
    
    notes = StringField("Tell us about the pet")
    available = BooleanField("Available?")