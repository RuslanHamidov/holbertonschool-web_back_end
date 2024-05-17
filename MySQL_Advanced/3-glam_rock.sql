-- SQL script that lists all bands with Glam rock as their main style
-- Script that performs task
SELECT band_name AS band_name, (split-formed) AS lifespan 
FROM metal_bands
ORDER BY lifespan DESC
WHERE style='Glam rock'
