-- to check if there is duplicate or not

-- Select movie_id, count(*) from tests.movie_production_countries
-- group by movie_id having count(*) > 1;

select distinct count(*) from tests.movies_spoken_languages; -- 53300 
select  count(*) from tests.movies_spoken_languages; -- 53300 

select distinct count(*) from tests.movie_collections; -- 4488 
select count(*) from tests.movie_collections; -- 4488 

select distinct count(*) from tests.movie_production_countries; -- 49423 
select count(*) from tests.movie_production_countries; -- 49423 

select distinct count(*) from tests.movies_production_companies; -- 804
select count(*) from tests.movies_production_companies; -- 804

select distinct count(*) from tests.movies_genre; -- 91015 
select count(*) from tests.movies_genre; -- 91015
