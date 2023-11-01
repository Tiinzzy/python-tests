from utility.Databases import Databases
from utility.OidGenerator import OidGenerator


class MoviesDao:
    MOVIE_COLLECTION = "movie"

    def __init__(self, title=None, release_date=None, rating=None, oid=None):
        if oid is None:
            self.oid = OidGenerator.get_new()
        else:
            self.oid = oid
        self.title = title
        self.release_date = release_date
        self.rating = rating
        self.db = Databases.NETFLIX

    def save_to_table(self):
        document = {
            "oid": self.oid,
            "movieTitle": self.title,
            "releaseDate": self.release_date,
            "rating": self.rating
        }
        if MoviesDao.id_exist(self.oid):
            self.db[self.MOVIE_COLLECTION].replace_one({"oid": self.oid}, document)
        else:
            self.db[self.MOVIE_COLLECTION].insert_one(document)

    @staticmethod
    def load_all():
        all_movie_dao = []
        for doc in Databases.NETFLIX.movie.find():
            movie = MoviesDao(oid=doc["oid"])
            movie.title = doc["movieTitle"]
            movie.release_date = doc["releaseDate"]
            movie.rating = doc["rating"]
            all_movie_dao.append({movie.oid: [movie.title, movie.release_date, movie.rating]})
        return all_movie_dao

    def delete(self, oid):
        self.db[self.MOVIE_COLLECTION].delete_one({"oid": oid})

    @staticmethod
    def id_exist(oid):
        all_ids = []
        for doc in Databases.NETFLIX.genre.find():
            movie = MoviesDao(oid=doc["oid"])
            movie.oid = doc["oid"]
            all_ids.append(movie.oid)
        if oid in all_ids:
            return True
        else:
            return False

    def get_oid(self):
        return self.oid

    def get_title(self):
        return self.title

    def get_release_date(self):
        return self.release_date

    def get_rating(self):
        return self.rating

    def set_title(self, title):
        self.title = title

    def set_release_date(self, release_date):
        self.release_date = release_date

    def set_rating(self, rating):
        self.rating = rating
