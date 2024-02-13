with source_data as (
    select
      ID,
      trim(coalesce(NAME, FULL_NAME)) as NAME,
      iff(NEO = 'Y', true, false) as NEO,
      iff(PHA = 'Y', true, false) as PHA,
      try_to_decimal(GM, 10, 5) / SQUARE(DIAMETER / 2) * 1000 as G,
      try_to_decimal(DIAMETER, 10, 5) / 2 as MEAN_RADIUS,
      try_to_decimal(A, 10, 5) as SEMIMAJOR_ORBIT,
      iff(SUBSTR(KIND, 1, 1) = 'a', 'Asteroid', 'Comet') as TYPE,
      CASE
        WHEN SEMIMAJOR_ORBIT < 2.0 THEN '0.0-2.0'
        WHEN SEMIMAJOR_ORBIT < 2.1 THEN '2.0-2.1'
        WHEN SEMIMAJOR_ORBIT < 2.2 THEN '2.1-2.2'
        WHEN SEMIMAJOR_ORBIT < 2.3 THEN '2.2-2.3'
        WHEN SEMIMAJOR_ORBIT < 2.4 THEN '2.3-2.4'
        WHEN SEMIMAJOR_ORBIT < 2.5 THEN '2.4-2.5'
        WHEN SEMIMAJOR_ORBIT < 2.6 THEN '2.5-2.6'
        WHEN SEMIMAJOR_ORBIT < 2.7 THEN '2.6-2.7'
        WHEN SEMIMAJOR_ORBIT < 2.8 THEN '2.7-2.8'
        WHEN SEMIMAJOR_ORBIT < 2.9 THEN '2.8-2.9'
        WHEN SEMIMAJOR_ORBIT < 3.0 THEN '2.9-3.0'
        WHEN SEMIMAJOR_ORBIT < 3.1 THEN '3.0-3.1'
        WHEN SEMIMAJOR_ORBIT < 3.2 THEN '3.1-3.2'
        WHEN SEMIMAJOR_ORBIT < 3.3 THEN '3.2-3.3'
        WHEN SEMIMAJOR_ORBIT < 3.4 THEN '3.3-3.4'
        WHEN SEMIMAJOR_ORBIT < 3.5 THEN '3.4-3.5'
        ELSE '3.5+'
      END AS DISTANCE_SPREAD
    from ANDY.PLUTO.SBDB
)

select *
from source_data
