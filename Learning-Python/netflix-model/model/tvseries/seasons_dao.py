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

    def load_all(self, tv_series_oid):
        seasons = self.db[self.SEASON_COLLECTION].find({"tvSeriesOid": tv_series_oid})
        print(seasons)
        all_seasons_of_a_tv_series_oid = []

        for doc in seasons:
            print(doc)
            s = SeasonDao(oid=doc["oid"])
            s.oid = doc["_id"]
            s.season_number = doc["seasonNumber"]
            s.start_date = doc["startDate"]
            s.end_date = doc["endDate"]
            s.tv_series_oid = doc["tvSeriesOid"]
            all_seasons_of_a_tv_series_oid.append(s)

        return all_seasons_of_a_tv_series_oid

    def load_by_oid(self, oid):
        season_data = self.db[self.SEASON_COLLECTION].find_one({"oid": oid})

        if season_data is not None:
            s = SeasonDao(oid=oid)
            s.oid = season_data["_id"]
            s.season_number = season_data["seasonNumber"]
            s.start_date = season_data["startDate"]
            s.end_date = season_data["endDate"]
            s.tv_series_oid = season_data["tvSeriesOid"]

            return s
        else:
            return None

    @staticmethod
    def id_exist(oid):
        all_ids = []
        for doc in Databases.NETFLIX.seasons.find():
            seasons = SeasonDao(oid=doc["oid"])
            seasons.oid = doc["oid"]
            all_ids.append(seasons.oid)
        print(oid)
        print(all_ids)
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
