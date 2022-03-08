from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AnimalForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///pet_adoption"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ihaveasecret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolabar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/')
def root():
    """Show recent list of posts, most-recent first."""
    pets = Pet.query.all()
    return render_template("index.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_snack():
    """Snack add form; handle adding."""

    form = AnimalForm()

    # if form.validate_on_submit():
    #     name = form.name.data
    #     species = form.species.data
    #     flash(f"Added {name} which is a {species}")
    #     return redirect("/")
    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        # new_pet = Pet(name=form.name.data, age=form.age.data, ...)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect('/')
    

    else:
        return render_template(
            "animal_add_form.html", form=form)


@app.route('/<int:id>/edit', methods=["GET", "POST"])
def edit_employee(id):
    pets = Pet.query.get_or_404(id)
    form = AnimalForm(obj=pets)

    if form.validate_on_submit():
        pets.name = form.name.data
        pets.species = form.species.data
        pets.available = form.available.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template("animal_add_form.html", form=form)