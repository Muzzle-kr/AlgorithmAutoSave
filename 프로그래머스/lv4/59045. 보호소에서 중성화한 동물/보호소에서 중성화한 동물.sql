-- 코드를 입력하세요
SELECT i.ANIMAL_ID, i.ANIMAL_TYPE, i.NAME
FROM ANIMAL_INS i JOIN ANIMAL_OUTS o
ON i.ANIMAL_ID = o.ANIMAL_ID
WHERE i.SEX_UPON_INTAKE LIKE 'Intact%'
AND o.SEX_UPON_OUTCOME REGEXP 'Spayed|Neutered'
ORDER BY 1




# 보호소에 들어올 당시에는 중성화 X
# 보호소를 나갈 당시에는 중성화된 동물
# 아이디와, 생물종, 이름 조회
# 아이디순