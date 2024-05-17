-- SQL script that ranks country origins of bands
-- Creates table band_fans
CREATE TABLE IF NOT EXISTS band_fans (
    origin VARCHAR(255),
    nb_fans INT
);
-- Inserts into fans
INSERT INTO band_fans (origin, nb_fans)
SELECT origin, fans
FROM metal_bands
ORDER BY fans DESC;
