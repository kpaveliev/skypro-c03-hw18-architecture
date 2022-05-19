from flask_restx import Resource, Namespace, fields
from flask import request
from marshmallow import ValidationError

from app.dao.model.movie import MovieSchema
from app.dao.model.genre import Genre
from app.dao.model.director import Director
from app.containter import movie_service

# Declare namespace and define marshmallow schema
movie_ns = Namespace('movies', description='Views for movies')
movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()

# Define api model for documentation
movie_model = movie_ns.model('Movie', {
    'id': fields.Integer(required=False, description="Movie identifier"),
    'title': fields.String(required=True, description="Movie title"),
    'description': fields.String(required=True, description="Short description"),
    'trailer': fields.String(required=True, description="Link to a trailer"),
    'year': fields.Integer(required=True, description="Release year"),
    'rating': fields.Float(required=True, description="Short description"),
    'genre_id': fields.Integer(required=True, description="Genre identifier"),
    'director_id': fields.Integer(required=True, description="Director identifier")
})


@movie_ns.route('/')
class MoviesViews(Resource):
    @movie_ns.doc(description='Get movies',
                  params={'director_id': 'Director identifier',
                          'genre_id': 'Genre identifier',
                          'year': 'Release year'})
    @movie_ns.response(200, 'Success', movie_model)
    @movie_ns.response(404, 'Not found')
    def get(self):
        # Get filter from request
        filters = {
            'director_id': request.args.get('director_id', type=int),
            'genre_id': request.args.get('genre_id', type=int),
            'year': request.args.get('year', type=int)
        }
        print(filters)
        movies_found = movie_service.filter(filters)

        if not movies_found:
            return f"No movies found with the specified parameters", 404

        return movies_schema.dump(movies_found), 200

    @movie_ns.doc(description='Add new director', body=movie_model)
    @movie_ns.response(201, 'Created')
    @movie_ns.response(400, 'ValidationError')
    def post(self):
        # Get data from request and serialize
        try:
            data = movie_schema.load(request.json)
        # Throw bad request wrong if fields passed
        except ValidationError as e:
            return f"{e}", 400
        # Add data to the database
        else:
            movie = movie_service.create(data)
            return f"Data added with id: {movie.id}", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route('/<int:uid>')
class MovieView(Resource):
    @movie_ns.doc(description='Get movie by id')
    @movie_ns.response(200, 'Success', movie_model)
    @movie_ns.response(404, 'Not found')
    def get(self, uid):
        # Find required row
        movie = movie_service.get_one(uid)
        # Throw not found if uid not found
        if not movie:
            return f"Movie with the id: {uid} not found", 404
        # Display found object
        else:
            return movie_schema.dump(movie), 200

    @movie_ns.doc(description='Update movie by id', body=movie_model)
    @movie_ns.response(200, 'Success')
    @movie_ns.response(400, 'Validation error')
    @movie_ns.response(404, 'Not found')
    def put(self, uid):
        # Get data from request and find object
        try:
            data = movie_schema.load(request.json)
            movie = movie_service.get_one(uid)
            if not movie:
                return f"Movie with the id: {uid} not found", 404

        # Throw bad request wrong if fields passed
        except ValidationError as e:
            return f"{e}", 400

        else:
            movie_service.update(uid, data)
            return f"Movie with id: {uid} successfully updated", 201

    @movie_ns.doc(description='Remove movie by id')
    @movie_ns.response(204, 'No content')
    @movie_ns.response(404, 'Not found')
    def delete(self, uid):
        # Find required row
        movie = movie_service.get_one(uid)
        # Throw not found if uid not found
        if not movie:
            return f"Movie with the id: {uid} not found", 404
        # Write deletion
        else:
            movie_service.delete(uid)
            return "", 204
