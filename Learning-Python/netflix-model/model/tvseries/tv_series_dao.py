from utility.Databases import Databases
from utility.OidGenerator import OidGenerator
from model.tvseries.seasons_dao import SeasonDao
from model.tvseries.episodes_dao import EpisodeDao


class TvSeriesDao:
    TV_SERIES_COLLECTION = "tv_series"

    def __init__(self, title=None, summary=None, startDate=None, endDate=None, oid=None):
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
        if TvSeriesDao.id_exist(self.oid):
            self.db[self.TV_SERIES_COLLECTION].replace_one(
                {"oid": self.oid}, document)
        else:
            self.db[self.TV_SERIES_COLLECTION].insert_one(document)

    @staticmethod
    def load_all(count=None):
        all_tv_series_dao = []
        query = Databases.NETFLIX.tv_series.find()
        if count is not None:
            query = query.limit(count)
        for doc in query:
            tv_series = TvSeriesDao(oid=doc["oid"])
            tv_series.title = doc["title"]
            tv_series.summary = doc["summary"]
            tv_series.startDate = doc["startDate"]
            tv_series.endDate = doc["endDate"]
            all_tv_series_dao.append(
                {tv_series.oid: [tv_series.title, tv_series.summary, tv_series.startDate, tv_series.endDate]})
        return all_tv_series_dao

    @staticmethod
    def load_by_oid(oid):
        selected_tv_series = []
        for doc in Databases.NETFLIX.tv_series.find({"oid": oid}):
            if doc["oid"] == oid:
                tv_series = TvSeriesDao(oid=doc["oid"])
                tv_series.title = doc["title"]
                tv_series.summary = doc["summary"]
                tv_series.startDate = doc["startDate"]
                tv_series.endDate = doc["endDate"]
                selected_tv_series.append(
                    {tv_series.oid: [tv_series.title, tv_series.summary, tv_series.startDate, tv_series.endDate]})
            return selected_tv_series
        return None

    @staticmethod
    def id_exist(oid):
        all_ids = []
        for doc in Databases.NETFLIX.genre.find():
            tv_series = TvSeriesDao(oid=doc["oid"])
            tv_series.oid = doc["oid"]
            all_ids.append(tv_series.oid)
        if oid in all_ids:
            return True
        else:
            return False

    def load_all_seasons(self):
        return SeasonDao.load_all(self.oid)

    def add_season(self, season_number, start_date, end_date):
        return SeasonDao(season_number, start_date, end_date, self.oid)

    @staticmethod
    def add_episode(seasonNumber, title, run_time, air_date):
        season = TvSeriesDao.get_season(seasonNumber)
        season_oid = season["oid"]
        return EpisodeDao(title, run_time, air_date, season_oid)

    def delete_season(self):
        return SeasonDao.delete(tvSeriesOid=self.oid)

    def delete_tv_series(self, oid):
        self.db[self.TV_SERIES_COLLECTION].delete_one({"oid": oid})

    @staticmethod
    def get_season(seasonNumber):
        seasons = SeasonDao.load_all()
        for s in seasons:
            if s["seasonNumber"] == seasonNumber:
                return s
            else:
                return None

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
