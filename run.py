from flask import Flask
from flask_restx import Api

from app.config import Config
from app.setup_db import db
from app.views.movies import movie_ns
from app.views.genres import genre_ns
from app.views.directors import director_ns


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    register_extensions(application)
    return application


def register_extensions(app: Flask) -> None:
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)


app_config = Config()
app = create_app(app_config)

if __name__ == '__main__':
    app.run()
