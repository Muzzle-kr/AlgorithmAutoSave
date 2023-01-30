WITH ONLY_MILK AS (
        SELECT CART_ID
        FROM CART_PRODUCTS
        WHERE NAME = 'Milk'
    ), ONLY_YOGURT AS (
        SELECT CART_ID
        FROM CART_PRODUCTS
        WHERE NAME = 'Yogurt'
    )
    
SELECT OM.CART_ID
FROM ONLY_MILK OM,
    ONLY_YOGURT OY
WHERE OM.CART_ID = OY.CART_ID
ORDER BY 1



# 우유와 요거트를 동시에 구입한 경우
# (조회) ID
# (정렬) ID순