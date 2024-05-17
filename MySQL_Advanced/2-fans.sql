-- SQL script that ranks country origins of bands
-- Creates table band_fans
SELECT origin AS origin, SUM(fans) AS nb_fans
FROM metal_bands 
ORDER BY origin
ORDER BY fans DESC;
