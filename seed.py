"""Seed file to make sample data for Users db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add users
one = Pet(name='Sonic',
          species="Hedgehog",
          notes="This poor teenage hedgehog needs a new home after an evil scientist demolish his world! Please adopt him!!")
two = Pet(name='Pepperoni', 
          species="Pig",
          photo_url="https://www.canr.msu.edu/contentAsset/image/9c8f1a21-90e3-486d-9ca0-dd4a7b4b439d/fileAsset/filter/Resize,Jpeg/resize_w/750/jpeg_q/80")
three = Pet(name='Butt', 
            species="Baboon", 
            photo_url="https://cdn.mos.cms.futurecdn.net/5VRpoZoyUuepUJi5kFTzmC.jpg" ,
            available=False)
four = Pet(name='Booty', 
           species="Gorilla", 
           photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Male_gorilla_in_SF_zoo.jpg/1200px-Male_gorilla_in_SF_zoo.jpg")

db.session.add_all([one, two, three, four])

# Commit--otherwise, this never gets saved!
db.session.commit()
