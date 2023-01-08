select * from tests.cities;

select city, country, lat, lng from tests.cities
order by country asc, lng desc;

select lat, '------', c.* from tests.cities c
where lat between -55 and -50 
order by lat;

select distinct country from tests.cities c
where lat between -55 and -50;

select c.* from tests.cities c
where (lat between -55 and -50) and (lng < -70);

select distinct city from tests.cities c
where country = 'Japan';

select distinct city, country from tests.cities c
where country = "Japan" or country = 'Iran' or country = 'Angola';

select distinct city, country from tests.cities c
where country in ('Japan', 'Iran', 'Angola');

select distinct country from tests.cities c
where left(country, 1) = 'J' and right(country, 1) = 'n';

select distinct country from tests.cities c
where lower(left(country, 1)) in ( 'j', 'i');

-- if you want to match with case, use like this
select distinct country from tests.cities c where country = BINARY 'japan';  -- this one is case sensitive
select distinct country from tests.cities c where country = 'japan';         -- but by default no matching is case sensitive

select * from tests.cities c where city like '%ch%g%';

select * from tests.cities c where population/1000000 > 2 order by population desc;

select * from tests.cities c where city in (select name from tests.city);

select * from tests.cities c where city in (select name from tests.city);

select country, count(*) CITY_COUNT, avg(population) AVG_POP, max(population) MAX_POP, min(population) MIN_POP from tests.cities 
group by country order by AVG_POP desc;

select * from (
	select distinct country as cf_name from tests.cities
	union
	select distinct film as cf_name from tests.movies
) as mixed_data    
where cf_name like '%ja%'
order by 1;

select * from (
	select distinct country as cf_name from tests.cities where country like '%ja%'
	union
	select distinct film as cf_name from tests.movies where film like '%ja%'
) as mixed_data    
order by 1;


