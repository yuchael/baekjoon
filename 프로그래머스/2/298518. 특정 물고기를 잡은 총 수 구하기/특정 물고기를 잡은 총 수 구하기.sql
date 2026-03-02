SELECT
        COUNT(id) AS fish_count
FROM 
        fish_info t1
    JOIN
        fish_name_info t2
    ON
        t1.fish_type = t2.fish_type
WHERE
        t2.fish_name = 'BASS' or t2.fish_name = 'snapper';