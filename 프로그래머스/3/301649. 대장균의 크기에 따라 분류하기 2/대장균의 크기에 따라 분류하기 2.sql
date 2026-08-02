SELECT
        ID,
        CASE
            WHEN  E.RANKING = 4  THEN  'CRITICAL'
            WHEN  E.RANKING = 3  THEN  'HIGH'
            WHEN  E.RANKING = 2  THEN  'MEDIUM'
            ELSE  'LOW'     
        END AS COLONY_NAME
FROM
        (SELECT     ID, SIZE_OF_COLONY, 
                    NTILE(4) OVER (ORDER BY SIZE_OF_COLONY) AS RANKING
        FROM        ECOLI_DATA) E
ORDER BY
        ID