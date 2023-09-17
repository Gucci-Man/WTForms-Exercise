from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Optional, URL, NumberRange
from wtforms import (
    StringField,
    TextAreaField,
    FloatField,
    BooleanField,
    IntegerField,
    RadioField,
    SelectField,
    URLField,
)


class PetForm(FlaskForm):
    """Form to add pet"""

    name = StringField(
        "Name", validators=[InputRequired(message="Pet name can't be blank")]
    )
    species = SelectField(
        "Species", choices=[("dog", "Dog"), ("cat", "Cat"), ("pcp", "Porcupine")]
    )
    photo = URLField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", validators=[Optional()])
