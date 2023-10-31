from utility.Databases import Databases
from utility.OidGenerator import OidGenerator

class TvSeriesDao:
    TV_SERIES_COLLECTION = "tv_series"

    def __init__(self, title=None, oid=None, summary=None, startDate=None, endDate=None):
        if oid is None:
            self.oid = OidGenerator.get_new()
        else:
            self.oid = oid
        self.title = title
        self.summary = summary
        self.startDate = startDate
        self.endDate = endDate
        self.db = Databases.NETFLIX

    def save_to_table(self):
        document = {
            "oid": self.oid,
            "title": self.title,
            "summary": self.summary,
            "startDate": self.startDate,
            "endDate": self.endDate
        }
        if (TvSeriesDao.__id_exist(self.oid)):
            self.db[self.TV_SERIES_COLLECTION].replace_one(
                {"oid": self.oid}, document)
        else:
            self.db[self.TV_SERIES_COLLECTION].insert_one(document)

    @staticmethod
    def load_all():
        all_tv_series_dao = []
        for doc in Databases.NETFLIX.tv_series.find():
            tv_series = TvSeriesDao(oid=doc["oid"])
            tv_series.title = doc["movieTitle"]
            tv_series.release_date = doc["releaseDate"]
            tv_series.rating = doc["rating"]
            all_tv_series_dao.append(tv_series)
        return all_tv_series_dao

    def delete_tv_series(self, oid):
        self.db[self.TV_SERIES_COLLECTION].delete_one({"oid": oid})

    @staticmethod
    def __id_exist(oid):
        temp = TvSeriesDao(oid=oid)
        return temp.get_oid() == oid
    

    def get_oid(self):
        return self.oid

    def get_title(self):
        return self.title

    def get_summary(self):
        return self.summary

    def get_startDate(self):
        return self.startDate

    def get_endDate(self):
        return self.endDate

    def set_title(self, title):
        self.title = title

    def set_summary(self, summary):
        self.summary = summary

    def set_startDate(self, startDate):
        self.startDate = startDate

    def set_endDate(self, endDate):
        self.endDate = endDate
