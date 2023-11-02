from utility.Databases import Databases
from utility.OidGenerator import OidGenerator


class EpisodeDao:
    EPISODE_COLLECTION = "episodes"

    def __init__(self, title=None, run_time=None, air_date=None, season_oid=None, oid=None):
        if oid is None:
            self.oid = OidGenerator.get_new()
        else:
            self.oid = oid
        self.title = title
        self.run_time = run_time
        self.air_date = air_date
        self.season_oid = season_oid
        self.db = Databases.NETFLIX

    def save_to_table(self):
        document = {
            "oid": self.oid,
            "title": self.title,
            "runTime": self.run_time,
            "airDate": self.air_date,
            "seasonOid": self.season_oid
        }
        if EpisodeDao.id_exist(self.oid):
            self.db[self.EPISODE_COLLECTION].replace_one(
                {"oid": self.oid}, document)
        else:
            self.db[self.EPISODE_COLLECTION].insert_one(document)

    def load_all(self, season_oid):
        episodes = self.db[self.EPISODE_COLLECTION].find(
            {"seasonOid": season_oid})
        all_episodes_of_a_season = []

        for doc in episodes:
            e = EpisodeDao(oid=doc["oid"])
            e.oid = doc["oid"]
            e.title = doc["title"]
            e.run_time = doc["runTime"]
            e.air_date = doc["airDate"]
            e.season_oid = doc["seasonOid"]
            all_episodes_of_a_season.append(e)

        return all_episodes_of_a_season

    def load_by_oid(self, oid):
        episode_data = self.db[self.EPISODE_COLLECTION].find_one({"oid": oid})

        if episode_data is not None:
            e = EpisodeDao(oid=oid)
            e.oid = episode_data["oid"]
            e.title = episode_data["title"]
            e.run_time = episode_data["runTime"]
            e.air_date = episode_data["airDate"]
            e.season_oid = episode_data["seasonOid"]
            return e
        else:
            return None

    @staticmethod
    def id_exist(oid):
        all_ids = []
        for doc in Databases.NETFLIX.episodes.find():
            episodes = EpisodeDao(oid=doc["oid"])
            episodes.oid = doc["oid"]
            all_ids.append(episodes.oid)
        if oid in all_ids:
            return True
        else:
            return False

    def get_oid(self):
        return self.oid

    def get_title(self):
        return self.title

    def get_run_time(self):
        return self.run_time

    def get_air_date(self):
        return self.air_date

    def get_season_oid(self):
        return self.season_oid
