# WITH MAX_FAVORITES AS (
#     SELECT
#         FOOD_TYPE,
#         MAX(FAVORITES) AS FAVORITES
#         FROM REST_INFO
#     GROUP BY FOOD_TYPE
# )

# SELECT * FROM MAX_FAVORITES;










# 음식 종류별로 즐겨찾기수가 가장 많은 식당
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM (
        SELECT *, rank() over(partition by FOOD_TYPE order by FAVORITES DESC) r
        FROM REST_INFO
    ) t
WHERE r = 1
ORDER BY FOOD_TYPE DESC















