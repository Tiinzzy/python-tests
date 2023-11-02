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

        loadNewEpisode = EpisodeDao.load_by_oid(oid=newEpisode.get_oid())
        print(loadNewEpisode)
