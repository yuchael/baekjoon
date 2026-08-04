SELECT
        ID, FISH_NAME, F1.LENGTH
FROM
        FISH_INFO F1
JOIN
        FISH_NAME_INFO F2
ON
        F1.FISH_TYPE = F2.FISH_TYPE
JOIN
        (
            SELECT      FISH_TYPE, MAX(IFNULL(LENGTH, 10)) AS LENGTH
            FROM        FISH_INFO
            GROUP BY    FISH_TYPE
        )M
ON
        F1.FISH_TYPE = M.FISH_TYPE

WHERE
        IFNULL(F1.LENGTH, 10) = M.LENGTH
ORDER BY
        ID
        
        