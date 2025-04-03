from flask import Blueprint, render_template, request, redirect, url_for
from flask import flash
from werkzeug.exceptions import abort

from msfsdb.db import db
from msfsdb.models import Aircraft, Category

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
    categories = Category.query.order_by(Category.name).all()

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
        print(f"saved aircraft {aircraft.name} to db")

        category_list = []
        for category in categories:
            if request.form[category.name] is not None:
                category_list.extend([
                    Category.query.filter_by(name=category.name).first()
                ])
        aircraft.categories = category_list
        db.session.commit()
        print(f"Saved category list to {aircraft.name}: {str(category_list)}")

        return redirect(url_for("aircraft.aircraft"))

    # print(f"Categories: {str(categories)}")
    return render_template(
        "aircraft/add.html",
        categories=categories
    )

@bp.route("/delete")
def delete_page():
    aircraft = Aircraft.query.order_by(Aircraft.name).all()
    return render_template(
        "aircraft/delete.html",
        aircraft=aircraft
    )

@bp.route("/delete/<int:id>", methods=("GET", "POST"))
def delete_aircraft(id):
    print("Aircraft id: " + str(id))

    if request.method == "POST":
        #then actually delete it and redirect
        aircraft = Aircraft.query.filter_by(id=id).first()
        if aircraft is None:
            abort(404, f"Aircraft with id {id} doesn't exist.")
        db.session.delete(aircraft)
        db.session.commit()
        print("deleted aircraft with id: " + str(id))
        return redirect(url_for("aircraft.delete_page"))

    return render_template(
        "aircraft/delete_confirm.html",
        id=id
    )