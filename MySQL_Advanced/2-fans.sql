-- SQL script that ranks country origins of bands
-- Creates table band_fans
SELECT origin AS origin, fans AS nb_fans
FROM metal_bands 
ORDER BY fans DESC;
