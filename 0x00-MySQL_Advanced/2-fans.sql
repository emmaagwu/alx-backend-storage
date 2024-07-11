-- SQL script to rank country origins of bands by the number of fans

-- SELECT statement to retrieve origin and sum of fans, aliasing the sum as nb_fans
SELECT origin AS origin,
  SUM(fans) AS nb_fans

-- FROM clause specifying the source table metal_bands
FROM metal_bands

-- WHERE clause to filter out rows where origin is NULL
WHERE origin IS NOT NULL

-- GROUP BY clause to group results by origin
GROUP BY origin

-- ORDER BY clause to order results by nb_fans in descending order
ORDER BY nb_fans DESC;