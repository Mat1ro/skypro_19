from flask_restx import Resource, Namespace

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        return "all genres", 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        return "one genre", 200
