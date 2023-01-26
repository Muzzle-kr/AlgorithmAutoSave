-- 코드를 입력하세요
# 아직 입양을 못간 동물 중
# 가장 오래 보호소에 있었던 동물
# 3마리의 이름과 보호시작일 조회
# 보호시작일 순

SELECT i.NAME, i.DATETIME
FROM ANIMAL_INS i LEFT OUTER JOIN ANIMAL_OUTS o
ON i.ANIMAL_ID = o.ANIMAL_ID
WHERE o.ANIMAL_ID IS NULL
ORDER BY 2
LIMIT 3

# SELECT * FROM ANIMAL_OUTS
# WHERE NAME REGEXP 'Jack|Disciple|Katie|Anna|Skips|Holly'

# SELECT * FROM ANIMAL_INS
# WHERE NAME REGEXP 'Jack|Disciple|Katie|Anna|Skips|Holly'