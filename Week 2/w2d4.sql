-- psql -d world -f w2d4.sql
-- \i w2d4.sql can run inside a terminal

-- select city.name as city_name, city.district as city_district, country.name  as country_name, float4((city.population)/float4(country.population))*100 as percentage from city, country  where city.countrycode = country.code and country.continent = 'Asia';

SELECT tag.id as tag_id, tag.name as tag_name, post.title as post_title
    FROM tag
    INNER JOIN post_tag
    ON (tag.id = post_tag.tag_id)
    INNER JOIN post
    ON (post_tag.post_id = post.id)
    WHERE post.title = 'First!';

SELECT tag.id as tag_id, tag.name as tag_name, post.title as post_title
    FROM tag
    INNER JOIN post_tag
    ON (tag.id = post_tag.tag_id and tag.id = 1)
    INNER JOIN post
    ON (post_tag.post_id = post.id);

SELECT tag.id as tag_id, tag.name as tag_name, post.title as post_title
    FROM tag
    INNER JOIN post_tag
    ON (tag.id = post_tag.tag_id)
    INNER JOIN post
    ON (post_tag.post_id = post.id)
    INNER JOIN author
    ON length(twitter) < 15;

