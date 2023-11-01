from utility.Databases import Databases
from utility.OidGenerator import OidGenerator


class GenreDao:
    GENRE_COLLECTION = "genre"

    def __init__(self, description=None, oid=None):
        if oid is None:
            self.oid = OidGenerator.get_new()
        else:
            self.oid = oid
        self.description = description
        self.db = Databases.NETFLIX

    def save_to_table(self):
        document = {
            "oid": self.oid,
            "description": self.description
        }
        if self.id_exist(self.oid):
            self.db[self.GENRE_COLLECTION].replace_one({"oid": self.oid}, document)
        else:
            self.db[self.GENRE_COLLECTION].insert_one(document)

    @staticmethod
    def load_all():
        all_genre_dao = []
        for doc in Databases.NETFLIX.genre.find():
            genre = GenreDao(oid=doc["oid"])
            genre.description = doc["description"]
            all_genre_dao.append({genre.oid: genre.description})
        return all_genre_dao

    def delete(self, oid):
        self.db[self.GENRE_COLLECTION].delete_one({"oid": oid})

    @staticmethod
    def id_exist(oid):
        all_ids = []
        for doc in Databases.NETFLIX.genre.find():
            genre = GenreDao(oid=doc["oid"])
            genre.oid = doc["oid"]
            all_ids.append(genre.oid)
        if oid in all_ids:
            return True
        else:
            return False
    
    def get_oid(self):
        return self.oid

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def __str__(self):
        return f"Genre: OID={self.oid}, Description={self.description}"
