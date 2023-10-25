from utility.Databases import Databases


class MoviesDao:
    MOVIE_COLLECTION = "movie"

    def __init__(self, title=None, oid=None, release_date=None, rating=None):
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

    def get_oid(self):
        return self.oid

    def get_title(self):
        return self.title

    def get_release_date(self):
        return self.release_date

    def get_rating(self):
        return self.rating
