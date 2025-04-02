from flask import Blueprint, render_template, request, redirect, url_for
from flask import flash
from msfsdb.db import db
from msfsdb.models import Aircraft

bp = Blueprint("aircraft", __name__, url_prefix="/aircraft")

@bp.route("/")
def aircraft():
    aircraft = Aircraft.query.order_by(Aircraft.name).all()
    print("Aircraft: " + str(aircraft[0].categories))

    return render_template(
        "aircraft/aircraft.html",
        aircraft=aircraft
    )

@bp.route("/add", methods=("GET", "POST"))
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

    return render_template("aircraft/add.html")

@bp.route("/delete", methods=("GET", "POST"))
def delete_page():
    aircraft = Aircraft.query.order_by(Aircraft.name).all()
    
    if request.method == "POST":

        return redirect(url_for("aircraft.aircraft"))
    
    return render_template(
        "aircraft/delete.html",
        aircraft=aircraft
    )

@bp.route("/delete/<int:id>", methods=("GET", "POST"))
def delete_aircraft(id):
    print("Aircraft id: " + str(id))

    if request.method == "POST":
        #then actually delete it and redirect
        print("not yet deleting aircraft with id: " + str(id))
        return redirect(url_for("aircraft.aircraft"))

    return render_template(
        "aircraft/delete_confirm.html",
        id=id
    )