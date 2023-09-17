from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import *
from forms import *

app = Flask(__name__)
app.app_context().push()

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "BATMAN1999FOREVER"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)

connect_db(app)

# Create tables
""" db.drop_all()
db.create_all() """


@app.route("/")
def home_page():
    """Home page that list the pets"""
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add():
    """Form to add pets"""
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo = form.photo.data
        if len(photo) == 0:
            photo = None  # if image_url is empty, then make it NULL, so default photo can be used

        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add_pet.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def details(pet_id):
    """Shows details of pet and allow edits"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm()

    if form.validate_on_submit():
        photo = form.photo.data

        # if new photo, then replace photo
        if len(photo) > 0:
            pet.photo_url = photo

        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        return redirect("/")
    else:
        return render_template("edit_pet.html", form=form, pet=pet)
