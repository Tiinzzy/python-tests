create view tests.movies_all_spoken_languages as 
select id, title, count(*), group_concat(language SEPARATOR ', ') languages from (
select m.id as id , title as title, sl.language as language
from tests.imbd_movies m
join tests.movies_spoken_languages msl on m.id = msl.movie_id
join tests.spoken_languages sl on sl.initial =msl.language_initial
) as T3
group by id, title;


-- to check see differences and avoid duplicates
-- select count(*) from tests.movies_spoken_languages
-- union all
-- select count(distinct movie_id, language_initial) from tests.movies_spoken_languages;
