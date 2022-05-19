from flask_restx import Resource, Namespace, fields

from app.dao.model.genre import GenreSchema
from app.containter import genre_service

# Declare namespace and define marshmallow schema
genre_ns = Namespace('genres', description='Views for genres')
genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()

# Define api model for documentation
genre_model = genre_ns.model('Genre', {
    'id': fields.Integer(required=False, description="Identifier"),
    'name': fields.String(required=True, description="Genre name")
})


@genre_ns.route('/')
class GenresViews(Resource):
    @genre_ns.doc(description='Get movies')
    @genre_ns.response(200, 'Success', genre_model)
    @genre_ns.response(404, 'Not found')
    def get(self):
        genres_found = genre_service.get_all()

        if not genres_found:
            return f"No genres found with the specified parameters", 404

        return genres_schema.dump(genres_found), 200


@genre_ns.route('/<int:uid>')
class GenreView(Resource):
    @genre_ns.doc(description='Get movie by id')
    @genre_ns.response(200, 'Success', genre_model)
    @genre_ns.response(404, 'Not found')
    def get(self, uid):
        # Find row
        genre = genre_service.get_one(uid)

        # Throw not found if uid not found
        if not genre:
            return f"Genre with the id: {uid} not found", 404

        else:
            return genre_schema.dump(genre), 200
