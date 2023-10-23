from utility.Database import Database


class GenreDao:
    GENRE_COLLECTION = "genre"

    def __init__(self, description=None, oid=None):
        self.oid = oid
        self.description = description
        self.db = Database().get_netflix_database()

    def save_to_table(self):
        document = {
            "oid": self.oid,
            "description": self.description
        }
        self.db[self.GENRE_COLLECTION].insert_one(document)

    @staticmethod
    def load_all():
        all_genre_dao = []
        for doc in Database().get_netflix_database().genre.find():
            genre = GenreDao(oid=doc["oid"])
            genre.description = doc["description"]
            all_genre_dao.append(genre)
        return all_genre_dao

    def get_oid(self):
        return self.oid

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description
