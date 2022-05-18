from .dao.movie import MovieDAO
from .service.movie import MovieService
from .setup_db import db

# Create DAOs
movie_dao = MovieDAO(session=db.session)


# Create services
movie_service = MovieService(movie_dao)