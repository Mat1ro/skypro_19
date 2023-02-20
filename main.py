from flask import Flask
from flask_restx import Api

from config import Config
from app.dao.model.director_model import Director
from app.dao.model.genre_model import Genre
from app.dao.model.movie_model import Movie
from setup_db import db
from app.views.director import director_ns
from app.views.genre import genre_ns
from app.views.movie import movie_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    create_data(app, db)


def create_data(app, db):
    with app.app_context():
        db.create_all()


app = create_app(Config())
app.url_map.strict_slashes = False

if __name__ == '__main__':
    app.run()
