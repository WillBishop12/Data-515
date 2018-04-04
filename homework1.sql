/* Homework 1 - Data 515
Will Bishop */

/* 
1. (3 points) Create a text file called homework1.sql that has SQL that operates on the class.db database in the Lectures repository. Your code should be in a text file that is executed by executeSQL.sh. The SQL should construct a query that returns data that contains the video_id, category_id, language (one of  ‘us’, ‘gb’, ‘fr’, ‘de’, ‘ca’).
*/

.open 'class.db'

SELECT video_id, category_id, 'ca' AS language FROM CAvideos
UNION
SELECT video_id, category_id, 'de' AS language FROM DEvideos
UNION
SELECT video_id, category_id, 'fr' AS language FROM FRvideos
UNION
SELECT video_id, category_id, 'gb' AS language FROM GBvideos
UNION
SELECT video_id, category_id, 'us' AS language FROM USvideos;


--Test code to find minimal keys
/*DROP VIEW answer;
CREATE VIEW answer AS
SELECT video_id, category_id, 'ca' AS language FROM CAvideos
UNION ALL
SELECT video_id, category_id, 'de' AS language FROM DEvideos
UNION ALL
SELECT video_id, category_id, 'fr' AS language FROM FRvideos
UNION ALL
SELECT video_id, category_id, 'gb' AS language FROM GBvideos
UNION ALL
SELECT video_id, category_id, 'us' AS language FROM USvideos;

SELECT COUNT(*) FROM answer; -- returns 35950
SELECT COUNT(DISTINCT video_id) FROM answer; -- returns 30697
SELECT COUNT(*) FROM (SELECT DISTINCT video_id, category_id FROM answer); -- returns 30724
SELECT COUNT(*) FROM (SELECT DISTINCT video_id, language FROM answer); -- returns 35920
SELECT COUNT(*) FROM (SELECT DISTINCT video_id, category_id, language FROM answer); -- returns 35950*/