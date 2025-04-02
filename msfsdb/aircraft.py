from flask import Blueprint, render_template, request, redirect, url_for
from flask import flash
from msfsdb.db import db
from msfsdb.models import Aircraft

bp = Blueprint("aircraft", __name__, url_prefix="/aircraft")

@bp.route("/")
def aircraft():
    aircraft = Aircraft.query.order_by(Aircraft.id).all()
    print("Aircraft: " + str(aircraft[0].categories))
    return render_template("aircraft.html",
    aircraft=aircraft)

@bp.route("/add_aircraft", methods=("GET", "POST"))
def add_aircraft():
    if request.method == "POST":
        try:
            aircraft = Aircraft(
                name=request.form['name'],
                description=request.form['description']
            )
        except ValueError as e:
            print(str(e))
            flash(str(e))
        
        db.session.add(aircraft)
        db.session.commit()
        print("saved to db")
        return redirect(url_for("aircraft.aircraft"))

    return render_template("add_aircraft.html")
