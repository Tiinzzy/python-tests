import unittest
from model.tvseries.tv_series_dao import TvSeriesDao
from model.tvseries.seasons_dao import SeasonDao
from model.tvseries.episodes_dao import EpisodeDao


class TestTvSeriesDao(unittest.TestCase):

    def test_save_to_table_tv_series_only(self):
        newTvSeries = TvSeriesDao("Tests Python", "this is a test to add from python", "1234", "5678")
        newTvSeries.save_to_table()
        self.assertTrue(newTvSeries.get_oid() != 0)
        self.assertTrue(newTvSeries.get_title(), "Tests Python")
        self.assertTrue(newTvSeries.get_summary(), "this is a test to add from python")
        self.assertTrue(newTvSeries.get_startDate(), "1234")
        self.assertTrue(newTvSeries.get_endDate(), "5678")

    def test_save_to_table_seasons(self):
        newSeason = SeasonDao(1, "1234", "5678", 678)
        newSeason.save_to_table()
        self.assertTrue(newSeason.get_oid() != 0)
        self.assertTrue(newSeason.get_season_number(), 1)
        self.assertTrue(newSeason.get_start_date(), "1234")
        self.assertTrue(newSeason.get_end_date(), "5678")
        self.assertTrue(newSeason.get_tv_series_oid(), 678)

    def test_save_to_table_episodes(self):
        newEpisode = EpisodeDao("python test 1", 1, "5678", 123)
        newEpisode.save_to_table()
        self.assertTrue(newEpisode.get_oid() != 0)
        self.assertTrue(newEpisode.get_title(), "python test 1")
        self.assertTrue(newEpisode.get_run_time(), 1)
        self.assertTrue(newEpisode.get_air_date(), "5678")
        self.assertTrue(newEpisode.get_season_oid(), 123)

    def test_load_episodes(self):
        load_all_episodes_with_season_id = EpisodeDao.load_all(123)
        self.assertTrue(len(load_all_episodes_with_season_id) > 0)

        all_episodes = EpisodeDao.load_all()
        self.assertTrue(len(all_episodes) > 0)

        oid = 308
        load_one_episode = EpisodeDao.load_by_oid(oid)
        key_variable = None
        value_variable = None
        for key, value in load_one_episode[0].items():
            key_variable = key
            value_variable = value
        self.assertTrue(key_variable, oid)
        self.assertTrue(value_variable[0], "From Pole to Pole")
        self.assertTrue(value_variable[1], 49)
        self.assertTrue(value_variable[2], "2006-03-05")
        self.assertTrue(value_variable[3], 10666)


