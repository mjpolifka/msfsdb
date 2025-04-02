from msfsdb.db import db

class Aircraft(db.Model):
    __tablename__ = 'Aircraft'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    categories = db.Relationship("Category", secondary='category_index', back_populates="aircraft")
    #TODO some kind of one-to-many or many-to-many for the category

    def __repr__(self):
        return f'<Aircraft {self.name}>'

class Category(db.Model):
    __tablename__ = 'Categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    aircraft = db.Relationship("Aircraft", secondary='category_index', back_populates="categories")

    def __repr__(self):
        return f'<Category {self.name}>'

# took this straight from the docs without really understanding it
# https://flask-sqlalchemy.readthedocs.io/en/stable/models/
# This link has the key:
# https://stackoverflow.com/questions/60950086/how-to-implement-many-to-many-relationship-using-flask-sqlalchemy
# I needed to add the db.Relationship lines above, I can't interact with this table directly
category_index = db.Table(
    "category_index",
    db.Column("aircraft_id", db.ForeignKey(Aircraft.id), primary_key=True),
    db.Column("category_id", db.ForeignKey(Category.id), primary_key=True)
)