from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


# MODELS GO BELOW!


class Pet(db.Model):
    """Pet model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(
        db.Text,
        default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSeNvCeCjX9KgEgNeTXOwE1WeAC7Ybm0OxHzA&usqp=CAU",
    )
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, default=True)
