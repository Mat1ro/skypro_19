from app.dao.director import DirectorDAO
from app.dao.genre import GenreDAO
from app.dao.movie import MovieDAO
from app.service.director import DirectorService
from app.service.genre import GenreService
from app.service.movie import MovieService
from app.service.user import UserService
from app.dao.user import UserDao
from app.service.auth import AuthService
from setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)


user_dao = UserDao(db.session)
user_service = UserService(user_dao)

auth_service = AuthService(user_service)