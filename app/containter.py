from .dao.movie import MovieDAO
from .dao.model.movie import MovieSchema
from .service.movie import MovieService
from .setup_db import db

# Create DAOs
movie_dao = MovieDAO(session=db.session)



# Create services
movie_service = MovieService(dao=movie_dao)