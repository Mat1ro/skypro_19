from flask_restx import Resource, Namespace
from flask import request
from app.dao.model.genre import GenreSchema
from container import genre_service
from app.helpers.decorations import auth_required, admin_required

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200

    @admin_required
    def post(self):
        req_json = request.json
        genre_service.create(req_json)
        return "Successfully", 201


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    @auth_required
    def get(self, gid):
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre), 200

    @admin_required
    def put(self, did):
        req_json = request.json
        req_json['id'] = did

        genre_service.update(req_json)
        return "Director was updated", 204

    @admin_required
    def delete(self, did):
        genre_service.delete(did)
        return "Movie was deleted", 204
