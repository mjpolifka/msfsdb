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
def add_category():
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

@bp.route("/delete")
def delete_page():
    categories = Category.query.order_by(Category.name).all()
    return render_template(
        "category/delete.html",
        categories=categories
    )

@bp.route("/delete/<int:id>", methods=("GET", "POST"))
def delete_category(id):
    print("Category id: " + str(id))

    if request.method == "POST":
        #then actually delete it and redirect
        category = Category.query.filter_by(id=id).first()
        if category is None:
            abort(404, f"Category with id {id} doesn't exist.")
        db.session.delete(category)
        db.session.commit()
        print("deleted category with id: " + str(id))
        return redirect(url_for("category.delete_page"))

    return render_template(
        "category/delete_confirm.html",
        id=id
    )