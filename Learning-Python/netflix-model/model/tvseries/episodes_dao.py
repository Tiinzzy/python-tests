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

    @staticmethod
    def load_all(season_oid=None):
        all_episodes_of_a_season = []
        for doc in Databases.NETFLIX.episodes.find():
            if doc["seasonOid"] == season_oid or season_oid == None:
                episode = EpisodeDao(oid=doc["oid"])
                episode.title = doc["title"]
                episode.run_time = doc["runTime"]
                episode.air_date = doc["airDate"]
                episode.season_oid = doc["seasonOid"]
                all_episodes_of_a_season.append(
                    {episode.oid: [episode.title, episode.run_time, episode.air_date, episode.season_oid]})
        return all_episodes_of_a_season

    @staticmethod
    def load_by_oid(oid):
        selected_episode = []
        for doc in Databases.NETFLIX.episodes.find():
            if doc["oid"] == oid:
                episode = EpisodeDao(oid=doc["oid"])
                episode.title = doc["title"]
                episode.run_time = doc["runTime"]
                episode.air_date = doc["airDate"]
                episode.season_oid = doc["seasonOid"]
                selected_episode.append(
                    {episode.oid: [episode.title, episode.run_time, episode.air_date, episode.season_oid]})
            return selected_episode
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

    @staticmethod
    def delete(oid):
        if EpisodeDao.id_exist(oid):
            Databases.NETFLIX.episodes.delete_one({"oid": oid})
            return True
        else:
            return False

    @staticmethod
    def delete_seasons_episode(seasonOid):
        try:
            Databases.NETFLIX.episodes.delete_many({"seasonOid": seasonOid})
        except:
            print("Unable to delete due to an error!")


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
