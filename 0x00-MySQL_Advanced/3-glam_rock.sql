-- SQL script to list bands with Glam rock style ranked by longevity

-- Select and calculate lifespan in years until 2022

SELECT band_name, 
       (IFNULL(split, '2020') - formed) AS lifespan
  FROM metal_bands
  WHERE FIND_IN_SET('Glam rock', IFNULL(style, "")) > 0
  ORDER BY lifespan DESC;
