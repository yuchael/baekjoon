SELECT      
        COUNT(ID) AS fish_count, MONTH(TIME) as month
FROM        
        fish_info
GROUP BY   
        MONTH(TIME)
ORDER BY
        month ASC
