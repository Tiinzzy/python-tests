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

    def test_load_seasons(self):
        s1 = SeasonDao(11, "1111-11-11", "1212-12-12", 666)
        s1.save_to_table()
        s2 = SeasonDao(12, "1111-11-11", "1212-12-12", 666)
        s2.save_to_table()
        self.assertTrue(s1.get_oid() != 0)
        self.assertTrue(s1.get_oid() != 2)
        load_all_seasons_with_tv_id = SeasonDao.load_all(666)
        self.assertTrue(len(load_all_seasons_with_tv_id) > 0)

        all_seasons = SeasonDao.load_all()
        self.assertTrue(len(all_seasons) > 0)

        oid = s1.get_oid()
        load_one_episode = SeasonDao.load_by_oid(oid)
        key_variable = None
        value_variable = None
        for key, value in load_one_episode[0].items():
            key_variable = key
            value_variable = value
        self.assertTrue(key_variable, oid)
        self.assertTrue(value_variable[0], 12)
        self.assertTrue(value_variable[1], "1111-11-11")
        self.assertTrue(value_variable[2], "1212-12-12")
        self.assertTrue(value_variable[3], 666)

    def test_load_tv_series(self):
        all_tv_series = TvSeriesDao.load_all()
        self.assertTrue(len(all_tv_series) > 0)

        load_10_tv_series = TvSeriesDao.load_all(10)
        self.assertTrue(len(load_10_tv_series) == 10)

        newTvSeries = TvSeriesDao("Tests Python10", "this is a test to add from python10", "4321", "8765")
        newTvSeries.save_to_table()
        self.assertTrue(newTvSeries.get_oid() != 0)
        self.assertTrue(newTvSeries.get_title(), "Tests Python10")

        key_variable = None
        value_variable = None
        load_new_tv_series = TvSeriesDao.load_by_oid(newTvSeries.get_oid())
        for key, value in load_new_tv_series[0].items():
            key_variable = key
            value_variable = value
        self.assertTrue(key_variable, newTvSeries.get_oid())
        self.assertTrue(value_variable[0], newTvSeries.get_title())
        self.assertTrue(value_variable[1], newTvSeries.get_summary())
        self.assertTrue(value_variable[2], newTvSeries.get_startDate())
        self.assertTrue(value_variable[3], newTvSeries.get_endDate())

        load_new_tv_series = TvSeriesDao.load_by_oid(66666)
        self.assertEquals(load_new_tv_series, None)


