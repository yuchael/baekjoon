SELECT
        count(id) as fish_count, MONTH(time) as month
FROM 
        fish_info
GROUP BY
        MONTH(time)
ORDER BY
        month
        
