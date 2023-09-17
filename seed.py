from models import *
from app import *

# Create all tables
db.drop_all()
db.create_all()

Pet.query.delete()

# Add sample pets into table pets
p1 = Pet(
    name="Gucci",
    species="dog",
    photo_url="data:image/jpeg;base64,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",
    age=15,
    available=False,
)

p2 = Pet(
    name="Mittens",
    species="cat",
    photo_url="data:image/jpeg;base64,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",
    age=5,
)

db.session.add_all([p1, p2])
db.session.commit()
