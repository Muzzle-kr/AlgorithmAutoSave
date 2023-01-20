# 같은 유저가 같은 상품을 구매했을 때..! 회원 ID 오름차순, 상품 ID 내림차순


SELECT USER_ID,
        PRODUCT_ID
        FROM ONLINE_SALE
        GROUP BY USER_ID, PRODUCT_ID
        HAVING COUNT(PRODUCT_ID) > 1
        ORDER BY USER_ID, PRODUCT_ID DESC
        
# SELECT * FROM ONLINE_SALE
# WHERE USER_ID = 6