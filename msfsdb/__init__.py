from flask import Flask
from msfsdb.db import db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI=f'sqlite:///database.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
    
    db.init_app(app)
    
    from msfsdb import index, aircraft, init_db
    app.register_blueprint(index.bp)
    app.register_blueprint(aircraft.bp)
    app.register_blueprint(init_db.bp)
    # app.register_blueprint(power.bp)
    
    return app