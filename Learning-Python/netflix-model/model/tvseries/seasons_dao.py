from utility.Databases import Databases
from utility.OidGenerator import OidGenerator
from model.tvseries.episodes_dao import EpisodeDao


class SeasonDao:
    SEASON_COLLECTION = "seasons"

    def __init__(self, season_number=None, start_date=None, end_date=None, tv_series_oid=None, oid=None):
        if oid is None:
            self.oid = OidGenerator.get_new()
        else:
            self.oid = oid
        self.season_number = season_number
        self.start_date = start_date
        self.end_date = end_date
        self.tv_series_oid = tv_series_oid
        self.db = Databases.NETFLIX

    def save_to_table(self):
        document = {
            "oid": self.oid,
            "seasonNumber": self.season_number,
            "startDate": self.start_date,
            "endDate": self.end_date,
            "tvSeriesOid": self.tv_series_oid
        }
        if SeasonDao.id_exist(self.oid):
            self.db[self.SEASON_COLLECTION].replace_one(
                {"oid": self.oid}, document)
        else:
            self.db[self.SEASON_COLLECTION].insert_one(document)

    @staticmethod
    def load_all(tv_series_oid=None):
        all_seaosns = []
        for doc in Databases.NETFLIX.seasons.find():
            if doc["tvSeriesOid"] == tv_series_oid or tv_series_oid == None:
                s = SeasonDao(oid=doc["oid"])
                s.season_number = doc["seasonNumber"]
                s.start_date = doc["startDate"]
                s.end_date = doc["endDate"]
                s.tv_series_oid = doc["tvSeriesOid"]
                all_seaosns.append(
                    {s.oid: [s.season_number, s.start_date, s.end_date, s.tv_series_oid]})
        return all_seaosns

    @staticmethod
    def load_by_oid(oid):
        selected_season = []
        for doc in Databases.NETFLIX.seasons.find({"oid": oid}):
            if doc["oid"] == oid:
                s = SeasonDao(oid=doc["oid"])
                s.season_number = doc["seasonNumber"]
                s.start_date = doc["startDate"]
                s.end_date = doc["endDate"]
                s.tv_series_oid = doc["tvSeriesOid"]
                selected_season.append(
                    {s.oid: [s.season_number, s.start_date, s.end_date, s.tv_series_oid]})
            return selected_season
        return None

    def load_episodes(self):
        return EpisodeDao.load_all(self.oid)

    def add_episode(self, title, run_time, air_date):
        new_episode = EpisodeDao(title, run_time, air_date, self.oid)
        new_episode.save_to_table()

    @staticmethod
    def delete_episode(episodeOid):
        EpisodeDao.delete(episodeOid)

    def delete_episodes(self):
        EpisodeDao.delete_seasons_episode(self.oid)

    def delete(self, seasonOid=None, tvSeriesOid=None):
        if SeasonDao.id_exist(seasonOid):
            EpisodeDao.delete_seasons_episode(seasonOid)
            if tvSeriesOid is not None:
                self.__delete_by_oid(tvSeriesOid)
            elif seasonOid is not None:
                self.__delete_by_oid(seasonOid)
            else:
                return False

    @staticmethod
    def id_exist(oid):
        all_ids = []
        for doc in Databases.NETFLIX.seasons.find():
            seasons = SeasonDao(oid=doc["oid"])
            seasons.oid = doc["oid"]
            all_ids.append(seasons.oid)
        if oid in all_ids:
            return True
        else:
            return False

    def get_oid(self):
        return self.oid

    def get_season_number(self):
        return self.season_number

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_tv_series_oid(self):
        return self.tv_series_oid

    def load_episodes(self):
        return EpisodeDao.load_all(self.oid)

    def add_episode(self, title, run_time, air_date):
        episode_dao = EpisodeDao(title, run_time, air_date, self.oid)
        episode_dao.save_to_table()

    @staticmethod
    def __delete_by_oid(oid):
        Databases.NETFLIX.SEASON_COLLECTION.delete_one({"oid": oid})

    @staticmethod
    def __delete_by_tv_series_id(tvSeriesOid):
        Databases.NETFLIX.SEASON_COLLECTION.delete_many({"tvSeriesOid": tvSeriesOid})
