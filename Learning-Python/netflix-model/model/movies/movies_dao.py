from utility.Databases import Databases
from utility.OidGenerator import OidGenerator


class MoviesDao:
    MOVIE_COLLECTION = "movie"

    def __init__(self, title=None, oid=None, release_date=None, rating=None):
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
        if(MoviesDao.__id_exist(self.oid)):
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
            all_movie_dao.append(movie)
        return all_movie_dao
    
    def delete_movie(self, oid):
        self.db[self.MOVIE_COLLECTION].delete_one({"oid": oid})

    @staticmethod
    def __id_exist(oid):
        temp = MoviesDao(oid=oid)
        return temp.get_oid() == oid

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

    def set_rating(self,rating):
        self.rating = rating