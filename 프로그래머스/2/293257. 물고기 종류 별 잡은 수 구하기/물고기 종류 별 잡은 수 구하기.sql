SELECT
        COUNT(id) as fish_count, fish_name
FROM
        fish_info t1
    JOIN
        fish_name_info t2
    on
        t1.fish_type = t2.fish_type
GROUP BY
        t2.fish_name
ORDER BY
        fish_count DESC;