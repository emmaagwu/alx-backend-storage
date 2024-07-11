-- SQL script to list bands with Glam rock style ranked by longevity

-- Select and calculate lifespan in years until 2022

SELECT band_name,
       IFNULL(2022 - formed - 2, 0) - IFNULL(2022 - split - 2, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC, band_name ASC;
