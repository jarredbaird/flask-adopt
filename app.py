"""Blogly application."""

from flask import Flask, render_template, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import PetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = 'platipus_eggs'
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def list_users():
    pets = Pet.query.all()
    return render_template('list-pets.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    form = PetForm()
    form.species.choices = [(pet.species, pet.species) for pet in Pet.query.all()]

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        flash(f"{name} the {species} added to list")
        db.session.add(Pet(name=name, 
                           species=species, 
                           photo_url=photo_url,
                           age=age,
                           notes=notes))
        db.session.commit()
        return redirect('/')
    
    else:
        return render_template('add-pet.html', form=form)

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def view_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)
    species = [(pet.species, pet.species) for pet in Pet.query.all()]
    form.species.choices = species

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.age = form.age.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    
    else:
        return render_template('edit-pet.html', form=form, pet=pet)