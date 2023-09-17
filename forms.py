from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Optional
from wtforms import (
    StringField,
    TextAreaField,
    FloatField,
    BooleanField,
    IntegerField,
    RadioField,
    SelectField,
)


# TODO - pet name(required), species(required), photo URL, age, notes
class PetForm(FlaskForm):
    """Form to add pet"""

    name = StringField(
        "Name", validators=[InputRequired(message="Pet name can't be blank")]
    )
    species = StringField(
        "Species", validators=[InputRequired(message="Species can't be blank")]
    )
    photo = StringField("Photo URL", validators=[Optional()])
    age = IntegerField("Age", validators=[Optional()])
    notes = TextAreaField("Notes", validators=[Optional()])
