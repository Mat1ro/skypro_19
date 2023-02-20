from flask_restx import Resource, Namespace

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        return "all movies", 200

    def post(self):
        return "new movie", 201


@movie_ns.route('<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        return "one movie", 200

    def put(self, mid):
        return "update movie", 204

    def patch(self, mid):
        return "partial update", 204

    def delete(self, mid):
        return "delete, film", 204
