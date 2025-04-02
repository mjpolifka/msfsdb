from flask import Blueprint, render_template

from msfsdb.db import db
from msfsdb.models import Aircraft, Category#, category_index

bp = Blueprint("init_db", __name__, url_prefix='/init_db')

@bp.route("/")
def init_db():
    db.drop_all()
    db.create_all()

    aircraft_list = []
    category_list = []

    # Create Aircraft
    c172 = Aircraft(name="C172", description="Cessna 172 Skyhawk")
    aircraft_list.extend([c172])

    db.session.add_all(aircraft_list)
    db.session.commit()


    # Create Categories
    ga = Category(name="GA", description="General Aviation")
    category_list.extend([ga])

    db.session.add_all(category_list)
    db.session.commit()


    # Assign Categories
    c172.categories = [ga]

    db.session.commit()

    return render_template("init_db.html")