from flask_restx import Resource, Namespace, fields

from app.dao.model.movie import MovieSchema
from app.dao.model.genre import Genre
from app.dao.model.director import Director
from app.containter import movie_service

# Declare namespace and define marshmallow schema
movie_ns = Namespace('movies', description='Views for movies')
movies_schema = MovieSchema(many=True)

# Define api model for documentation
movie_model = movie_ns.model('Movie', {
    'id': fields.Integer(required=True, description="Movie identifier"),
    'title': fields.String(required=True, description="Movie title"),
    'description': fields.String(required=True, description="Short description"),
    'trailer': fields.String(required=True, description="Link to a trailer"),
    'year': fields.Integer(required=True, description="Release year"),
    'rating': fields.Float(required=True, description="Short description"),
    'genre_id': fields.String(required=True, description="Genre identifier"),
    'director_id': fields.String(required=True, description="Director identifier"),
    'genre': fields.String(required=False, description="Genre name"),
    'director': fields.String(required=False, description="Director name"),
})



@movie_ns.route('/')
class MoviesViews(Resource):
    @movie_ns.doc(description='Get movies')
    @movie_ns.response(200, 'Success', movie_model)
    @movie_ns.response(404, 'Not found')
    def get(self):
        # movies_all = Movie.query.all()
        movies_all = movie_service.get_all()
        return movies_schema.dump(movies_all)