from flask_restx import Resource, Namespace, fields

from app.dao.model.director import DirectorSchema
from app.containter import director_service

# Declare namespace and define marshmallow schema
director_ns = Namespace('directors', description='Views for directors')
directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()

# Define api model for documentation
director_model = director_ns.model('Director', {
    'id': fields.Integer(required=False, description="Identifier"),
    'name': fields.String(required=True, description="Director name")
})


@director_ns.route('/')
class DirectorsViews(Resource):
    @director_ns.doc(description='Get movies')
    @director_ns.response(200, 'Success', director_model)
    @director_ns.response(404, 'Not found')
    def get(self):
        directors_found = director_service.get_all()

        if not directors_found:
            return f"No directors found with the specified parameters", 404

        return directors_schema.dump(directors_found), 200


@director_ns.route('/<int:uid>')
class DirectorView(Resource):
    @director_ns.doc(description='Get movie by id')
    @director_ns.response(200, 'Success', director_model)
    @director_ns.response(404, 'Not found')
    def get(self, uid):
        # Find row
        director = director_service.get_one(uid)

        # Throw not found if uid not found
        if not director:
            return f"Director with the id: {uid} not found", 404

        else:
            return director_schema.dump(director), 200
