from flask import Blueprint, render_template, request, redirect, url_for
from flask import flash
from werkzeug.exceptions import abort

from msfsdb.db import db
from msfsdb.models import Aircraft, Category

bp = Blueprint("category", __name__, url_prefix="/category")

@bp.route("/")
def category():
    categories = Category.query.order_by(Category.name).all()
    # print("Categories: " + str(categories))

    return render_template(
        "category/category.html",
        categories=categories
    )

@bp.route("/add", methods=("GET", "POST"))
def add_aircraft():
    aircraft = Aircraft.query.order_by(Aircraft.name).all()

    if request.method == "POST":
        try:
            category = Category(
                name=request.form['name'],
                description=request.form['description']
            )
        except ValueError as e:
            print(str(e))
            flash(str(e))
        
        db.session.add(category)
        db.session.commit()
        print(f"saved category { category.name } to db")

        aircraft_list = []
        for item in request.form:
            for craft in aircraft:
                if str(item) == craft.name:
                    aircraft_list.extend([
                        Aircraft.query.filter_by(name=craft.name).first()
                    ])
        category.aircraft = aircraft_list
        db.session.commit()
        # print(f"Aircraft list: {str(aircraft_list)}")
        print(f"Saved aircraft list to {category.name}: {str(aircraft_list)}")

        return redirect(url_for("category.category"))

    return render_template(
        "category/add.html",
        aircraft=aircraft
    )
"""
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
        aircraft = Aircraft.query.filter_by(id=id).first()
        if aircraft is None:
            abort(404, f"Aircraft with id {id} doesn't exist.")
        db.session.delete(aircraft)
        db.session.commit()
        print("deleted aircraft with id: " + str(id))
        return redirect(url_for("aircraft.aircraft"))

    return render_template(
        "aircraft/delete_confirm.html",
        id=id
    )
"""