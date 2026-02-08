SELECT
        CONCAT(QUARTER(differentiation_date), 'Q') AS QUARTER, COUNT(id) AS ecoli_count
FROM
        ecoli_data
GROUP BY
        CONCAT(QUARTER(DIFFERENTIATION_DATE), 'Q')
ORDER BY
        QUARTER